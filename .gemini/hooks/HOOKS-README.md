# HOOKS-README

Scripts, sound folders, and configuration for the Gemini CLI hook handler.

## Hook Events Overview — [Official 11 Hooks](https://geminicli.com/docs/hooks/)

Gemini CLI fires 11 hook events across the session / agent / model / tool lifecycle:

| # | Hook | Description |
|:-:|------|-------------|
| 1 | `SessionStart` | A session begins (startup, resume, clear) |
| 2 | `SessionEnd` | A session ends (exit, clear) |
| 3 | `BeforeAgent` | User submits a prompt, before planning begins |
| 4 | `AfterAgent` | Agent loop ends |
| 5 | `BeforeModel` | Before a request is sent to the LLM |
| 6 | `AfterModel` | After a response is received from the LLM |
| 7 | `BeforeToolSelection` | Before the LLM selects which tools to call |
| 8 | `BeforeTool` | Before a tool executes (can block) |
| 9 | `AfterTool` | After a tool finishes executing |
| 10 | `PreCompress` | Before context compression runs |
| 11 | `Notification` | A system notification is emitted |

### Mapping from Claude Code Hooks

Six of the eleven Gemini hooks have a direct Claude Code analog; the other five are Gemini-specific:

| Gemini hook | Claude Code analog | Sound folder source |
|-------------|-------------------|---------------------|
| `SessionStart` | `SessionStart` | reused |
| `SessionEnd` | `SessionEnd` | reused |
| `BeforeTool` | `PreToolUse` | reused (renamed from `pretooluse/`) |
| `AfterTool` | `PostToolUse` | reused (renamed from `posttooluse/`) |
| `PreCompress` | `PreCompact` | reused (renamed from `precompact/`) |
| `Notification` | `Notification` | reused |
| `BeforeAgent` | — | placeholder (replace with your own sound) |
| `AfterAgent` | — | placeholder |
| `BeforeModel` | — | placeholder |
| `AfterModel` | — | placeholder |
| `BeforeToolSelection` | — | placeholder |

## Prerequisites

- **Python 3** — verify with `python3 --version`
- Audio player (auto-detected per platform):
  - **macOS**: `afplay` (built-in)
  - **Linux**: `paplay` / `aplay` / `ffplay` / `mpg123` (first available)
  - **Windows**: built-in `winsound` module (WAV only)

## How Hooks Are Executed

Hooks are configured in `.gemini/settings.json` to run with Python 3:

```json
{
  "type": "command",
  "command": "python3 .gemini/hooks/scripts/hooks.py",
  "timeout": 5000
}
```

Gemini CLI sends a JSON payload to the script on stdin containing at least:

| Field | Description |
|-------|-------------|
| `hook_event_name` | Which hook fired (e.g. `"BeforeTool"`, `"SessionStart"`) |
| `session_id` | Current session identifier |
| `transcript_path` | Path to the transcript file |
| `cwd` | Current working directory |
| `timestamp` | ISO-8601 timestamp |

Tool hooks (`BeforeTool`, `AfterTool`, `BeforeToolSelection`) additionally include `tool_name` and `tool_input`.

The script exits 0 on every path so it never blocks Gemini's work.

## Sound Folders

Each hook has a corresponding folder under `.gemini/hooks/sounds/` containing `<hookname>.mp3` and `<hookname>.wav` (lowercased hook name). The script tries `.wav` first, then `.mp3`.

```
.gemini/hooks/sounds/
  sessionstart/sessionstart.{wav,mp3}
  sessionend/sessionend.{wav,mp3}
  beforeagent/beforeagent.{wav,mp3}        ← placeholder
  afteragent/afteragent.{wav,mp3}          ← placeholder
  beforemodel/beforemodel.{wav,mp3}        ← placeholder
  aftermodel/aftermodel.{wav,mp3}          ← placeholder
  beforetoolselection/beforetoolselection.{wav,mp3}  ← placeholder
  beforetool/beforetool.{wav,mp3}
  beforetool/beforetool-git-committing.{wav,mp3}     ← special sound on git commit
  aftertool/aftertool.{wav,mp3}
  precompress/precompress.{wav,mp3}
  notification/notification.{wav,mp3}
```

### Special Case: Git Commit Sound

When `BeforeTool` fires for a shell tool (`Bash` or `run_shell_command`) and the command matches `git commit`, the script plays `beforetool/beforetool-git-committing.{wav,mp3}` instead of the default `BeforeTool` sound.

## Enabling / Disabling Hooks

### Disable All Hooks

Edit `.gemini/settings.json` and set `"disableAllHooks": true`. The settings file is shared in git; for personal overrides, edit `.gemini/settings.local.json` (git-ignored).

### Disable Individual Hooks

Edit `.gemini/hooks/config/hooks-config.json`:

```json
{
  "disableSessionStartHook": false,
  "disableBeforeToolHook": false,
  "disableAfterToolHook": false,
  "disableLogging": true
}
```

For personal overrides, create `.gemini/hooks/config/hooks-config.local.json` (git-ignored). Local values win over shared values; missing keys fall through to the shared file.

### Logging

Set `disableLogging: false` to append every hook's stdin payload to `.gemini/hooks/logs/hooks-log.jsonl` (useful for debugging; `transcript_path` and `cwd` are stripped from log entries).

## Text to Speech (TTS)

Website used to generate sounds: https://elevenlabs.io/
Voice used: Samara X
