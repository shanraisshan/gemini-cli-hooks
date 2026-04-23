# Installation — Windows

[⬅ Back to Main README](../README.md)

## Prerequisites

- **Python 3**
  - Verify (PowerShell): `python --version`
  - Install: `winget install Python.Python.3` or download from [python.org](https://www.python.org/downloads/)
  - Make sure "Add Python to PATH" is checked during installation.
- **Audio Player**: built-in `winsound` module (ships with Python). Only `.wav` files are played on Windows.

All details are in [HOOKS-README.md](../.gemini/hooks/HOOKS-README.md).

---

## Installation

### Step 1: Copy the hooks folder

From PowerShell in your project directory:

```powershell
mkdir .gemini\hooks -ErrorAction SilentlyContinue
git clone https://github.com/shanraisshan/gemini-cli-hooks.git temp-hooks
Copy-Item -Recurse temp-hooks\.gemini\hooks\* .gemini\hooks\
Remove-Item -Recurse -Force temp-hooks
```

### Step 2: Merge settings.json

1. If you don't have `.gemini\settings.json`, create one.
2. Open [`install/settings-windows.json`](settings-windows.json) and merge the `disableAllHooks` and `hooks` keys into your `.gemini\settings.json`.

> **Why a Windows-specific settings file?**
> - Python command is `python` on Windows (vs. `python3` on macOS/Linux).

### Step 3: Start Gemini CLI

```powershell
gemini
```

You should hear the SessionStart sound on startup.

### Note on audio formats

On Windows, only `.wav` files play via `winsound`. The repo ships both `.wav` and `.mp3` for every hook, so no action is needed.
