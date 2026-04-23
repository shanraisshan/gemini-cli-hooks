# Installation — Linux

[⬅ Back to Main README](../README.md)

## Prerequisites

- **Python 3**
  - Verify: `python3 --version`
  - Install (Debian/Ubuntu): `sudo apt install python3`
  - Install (RHEL/CentOS): `sudo yum install python3`
- **Audio Player**: one of `paplay`, `aplay`, `ffplay`, `mpg123` (first available is used)
  - Recommended: `sudo apt install pulseaudio-utils` (provides `paplay`)

All details are in [HOOKS-README.md](../.gemini/hooks/HOOKS-README.md).

---

## Installation

### Step 1: Copy the hooks folder

```bash
mkdir -p .gemini/hooks
git clone https://github.com/shanraisshan/gemini-cli-hooks.git temp-hooks
cp -r temp-hooks/.gemini/hooks/* .gemini/hooks/
rm -rf temp-hooks
```

### Step 2: Merge settings.json

1. If you don't have `.gemini/settings.json`, create one: `touch .gemini/settings.json`
2. Open [`install/settings-linux.json`](settings-linux.json) and merge the `disableAllHooks` and `hooks` keys into your `.gemini/settings.json`.

### Step 3: Start Gemini CLI

```bash
gemini
```

You should hear the SessionStart sound on startup.
