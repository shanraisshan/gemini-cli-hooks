# Gemini CLI Hooks
[![Hooks](https://img.shields.io/badge/supports%20all-11%20hooks-white?style=flat&labelColor=555)](https://github.com/shanraisshan/gemini-cli-hooks/blob/main/.gemini/hooks/HOOKS-README.md#hook-events-overview--official-11-hooks) [![Version](https://img.shields.io/badge/updated%20with%20Gemini%20CLI-v0.43.0%20(May%2026%2C%202026%2009:36%20PM%20PKT)-white?style=flat&labelColor=555)](https://github.com/google-gemini/gemini-cli/releases) [![Stars](https://img.shields.io/github/stars/shanraisshan/gemini-cli-hooks?style=flat&label=%E2%98%85&labelColor=555&color=white)](https://github.com/shanraisshan/gemini-cli-hooks)

<p align="center">
  <img src="!/gemini-speaking.svg" alt="Gemini CLI mascot speaking" width="176" height="158">
</p>

<p align="center">
  <img src="!/repo-description.svg" alt="Sound notifications for every Gemini CLI hook event — session, agent, model, and tool lifecycle" height="56">
</p>

## Installation

<p>
  <a href="install/README-mac.md"><img src="!/pill-mac.svg" alt="Mac" height="36"></a>&nbsp;
  <a href="install/README-linux.md"><img src="!/pill-linux.svg" alt="Linux" height="36"></a>&nbsp;
  <a href="install/README-windows.md"><img src="!/pill-windows.svg" alt="Windows" height="36"></a>
</p>

![How to Use](!/how-to-use.svg)

**Step 1.** Start Gemini CLI:
```bash
gemini
```

**Step 2.** Send a prompt (e.g., `Hi`) — you'll hear a sound on session start, tool use, agent response, and more.

## Common Errors

If prerequisites are missing, you'll see an error on Gemini CLI start:

```
SessionStart hook error
```

Verify Python 3 is installed (`python3 --version`) and that `.gemini/hooks/scripts/hooks.py` exists in your project.

## Changelog

| Date | Hooks | Changes | Gemini CLI Version |
|------|:-----:|---------|:------------------:|
| Apr 22, 2026 | 11 | Initial release: all 11 Gemini CLI hooks (`SessionStart`, `SessionEnd`, `BeforeAgent`, `AfterAgent`, `BeforeModel`, `AfterModel`, `BeforeToolSelection`, `BeforeTool`, `AfterTool`, `PreCompress`, `Notification`) | [v0.38.2](https://github.com/google-gemini/gemini-cli/releases) |

## Other Repos

<table>
<tr>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/claude-code-hooks"><img src="!/claude-speaking.svg" alt="Claude Code Hooks" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/claude-code-hooks"><strong>Claude Code<br>Hooks</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/codex-cli-hooks"><img src="!/codex-speaking.svg" alt="Codex CLI Hooks" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/codex-cli-hooks"><strong>Codex CLI<br>Hooks</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/claude-code-best-practice"><img src="!/claude-jumping.svg" alt="Claude Code Best Practice" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/claude-code-best-practice"><strong>Claude Code<br>Best Practice</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/gemini-cli-best-practice"><img src="!/gemini-jumping.svg" alt="Gemini CLI Best Practice" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/gemini-cli-best-practice"><strong>Gemini CLI<br>Best Practice</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/codex-cli-best-practice"><img src="!/codex-jumping.svg" alt="Codex CLI Best Practice" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/codex-cli-best-practice"><strong>Codex CLI<br>Best Practice</strong></a>
</td>
</tr>
</table>

## <img src="!/tags/sponsor-heart.svg" width="22" height="22" align="center"> Sponsor My Work

If you like my work, buy me a doodh patti 🍵 on

<a href="https://buy.polar.sh/polar_cl_7uBOTcVcWZDFuFUnzNeWftmbHi2gLv4Nawz892SiTa8"><img src="!/tags/polar.svg" alt="Polar" width="40" height="40" align="center"></a> <a href="https://buy.polar.sh/polar_cl_7uBOTcVcWZDFuFUnzNeWftmbHi2gLv4Nawz892SiTa8"><strong>Polar</strong></a>
