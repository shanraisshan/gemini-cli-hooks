# Installation — macOS

[⬅ Back to Main README](../README.md)

## Prerequisites

- **Python 3**
  - Verify: `python3 --version`
  - Install: `brew install python3` (requires [Homebrew](https://brew.sh/))
- **Audio Player**: `afplay` (built-in on macOS)

All details are in [HOOKS-README.md](../.gemini/hooks/HOOKS-README.md).

---

## Installation

### Step 1: Copy the hooks folder

From your project directory:

```bash
mkdir -p .gemini/hooks
git clone https://github.com/shanraisshan/gemini-cli-hooks.git temp-hooks
cp -r temp-hooks/.gemini/hooks/* .gemini/hooks/
rm -rf temp-hooks
```

### Step 2: Merge settings.json

1. If you don't have `.gemini/settings.json`, create one: `touch .gemini/settings.json`
2. Open [`install/settings-mac.json`](settings-mac.json) and merge the `disableAllHooks` and `hooks` keys into your `.gemini/settings.json`.

> **Why separate per-platform settings?**
> - Python command: `python3` (macOS / Linux) vs. `python` (Windows)

### Step 3: Start Gemini CLI

```bash
gemini
```

You should hear the SessionStart sound on startup, and further sounds as tools run and the session progresses.
