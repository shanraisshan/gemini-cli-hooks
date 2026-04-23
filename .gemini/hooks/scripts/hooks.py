#!/usr/bin/env python3
"""
Gemini CLI Hook Handler
=============================================
This script handles events from Gemini CLI and plays sounds for different hook events.
Supports all 11 Gemini CLI hooks: https://geminicli.com/docs/hooks/

Special handling for git commits: plays beforetool-git-committing.mp3
"""

import sys
import json
import subprocess
import re
import platform
from pathlib import Path

try:
    import winsound
except ImportError:
    winsound = None

# ===== HOOK EVENT TO SOUND FOLDER MAPPING =====
HOOK_SOUND_MAP = {
    "SessionStart": "sessionstart",
    "SessionEnd": "sessionend",
    "BeforeAgent": "beforeagent",
    "AfterAgent": "afteragent",
    "BeforeModel": "beforemodel",
    "AfterModel": "aftermodel",
    "BeforeToolSelection": "beforetoolselection",
    "BeforeTool": "beforetool",
    "AfterTool": "aftertool",
    "PreCompress": "precompress",
    "Notification": "notification",
}

# ===== BASH COMMAND PATTERNS =====
BASH_PATTERNS = [
    (r'git commit', "beforetool-git-committing"),
]


def get_audio_player():
    system = platform.system()

    if system == "Darwin":
        return ["afplay"]
    elif system == "Linux":
        players = [
            ["paplay"],
            ["aplay"],
            ["ffplay", "-nodisp", "-autoexit"],
            ["mpg123", "-q"],
        ]
        for player in players:
            try:
                subprocess.run(
                    ["which", player[0]],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=True,
                )
                return player
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
        return None
    elif system == "Windows":
        return ["WINDOWS"]
    else:
        return None


def play_sound(sound_name):
    if "/" in sound_name or "\\" in sound_name or ".." in sound_name:
        print(f"Invalid sound name: {sound_name}", file=sys.stderr)
        return False

    audio_player = get_audio_player()
    if not audio_player:
        return False

    script_dir = Path(__file__).parent
    hooks_dir = script_dir.parent

    folder_name = sound_name.split('-')[0]
    sounds_dir = hooks_dir / "sounds" / folder_name

    is_windows = audio_player[0] == "WINDOWS"
    extensions = ['.wav'] if is_windows else ['.wav', '.mp3']

    for extension in extensions:
        file_path = sounds_dir / f"{sound_name}{extension}"
        if file_path.exists():
            try:
                if is_windows:
                    if winsound:
                        winsound.PlaySound(
                            str(file_path),
                            winsound.SND_FILENAME | winsound.SND_NODEFAULT,
                        )
                        return True
                    return False
                else:
                    subprocess.Popen(
                        audio_player + [str(file_path)],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        start_new_session=True,
                    )
                    return True
            except (FileNotFoundError, OSError) as e:
                print(f"Error playing sound {file_path.name}: {e}", file=sys.stderr)
                return False
            except Exception as e:
                print(f"Error playing sound {file_path.name}: {e}", file=sys.stderr)
                return False

    return False


def _load_config_pair():
    script_dir = Path(__file__).parent
    hooks_dir = script_dir.parent
    config_dir = hooks_dir / "config"

    local_path = config_dir / "hooks-config.local.json"
    default_path = config_dir / "hooks-config.json"

    def _read(path):
        if not path.exists():
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading {path.name}: {e}", file=sys.stderr)
            return None

    return _read(local_path), _read(default_path)


def is_hook_disabled(event_name):
    try:
        local_config, default_config = _load_config_pair()
        key = f"disable{event_name}Hook"

        if local_config is not None and key in local_config:
            return local_config[key]
        if default_config is not None and key in default_config:
            return default_config[key]
        return False
    except Exception as e:
        print(f"Error in is_hook_disabled: {e}", file=sys.stderr)
        return False


def is_logging_disabled():
    try:
        local_config, default_config = _load_config_pair()
        if local_config is not None and "disableLogging" in local_config:
            return local_config["disableLogging"]
        if default_config is not None and "disableLogging" in default_config:
            return default_config["disableLogging"]
        return False
    except Exception as e:
        print(f"Error in is_logging_disabled: {e}", file=sys.stderr)
        return False


def log_hook_data(hook_data):
    if is_logging_disabled():
        return

    try:
        script_dir = Path(__file__).parent
        hooks_dir = script_dir.parent
        logs_dir = hooks_dir / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)

        log_entry = hook_data.copy()
        log_entry.pop("transcript_path", None)
        log_entry.pop("cwd", None)

        log_path = logs_dir / "hooks-log.jsonl"
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(log_entry, ensure_ascii=False, indent=2) + "\n")
    except Exception as e:
        print(f"Failed to log hook_data: {e}", file=sys.stderr)


def detect_bash_command_sound(command):
    if not command:
        return None
    for pattern, sound_name in BASH_PATTERNS:
        if re.search(pattern, command.strip()):
            return sound_name
    return None


def get_sound_name(hook_data):
    event_name = hook_data.get("hook_event_name", "")
    tool_name = hook_data.get("tool_name", "")

    if event_name == "BeforeTool" and tool_name in ("Bash", "run_shell_command"):
        tool_input = hook_data.get("tool_input", {}) or {}
        command = tool_input.get("command", "")
        special_sound = detect_bash_command_sound(command)
        if special_sound:
            return special_sound

    return HOOK_SOUND_MAP.get(event_name)


def main():
    try:
        stdin_content = sys.stdin.read().strip()
        if not stdin_content:
            sys.exit(0)

        input_data = json.loads(stdin_content)
        log_hook_data(input_data)

        event_name = input_data.get("hook_event_name", "")
        if is_hook_disabled(event_name):
            sys.exit(0)

        sound_name = get_sound_name(input_data)
        if sound_name:
            play_sound(sound_name)

        sys.exit(0)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
