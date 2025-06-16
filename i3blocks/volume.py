#!/usr/bin/env python3

import subprocess
import re

def get_default_sink():
    result = subprocess.run(["pactl", "get-default-sink"], capture_output=True, text=True)
    return result.stdout.strip()

def get_volume():
    sink = get_default_sink()
    if not sink:
        return "No sink"

    try:
        output = subprocess.check_output(["pactl", "list", "sinks"], text=True)
        blocks = output.split("Sink #")[1:]  # skip the header
        for block in blocks:
            if f"Name: {sink}" in block:
                # Volume
                match = re.search(r"Volume:.*?(\d+)%", block)
                volume = int(match.group(1)) if match else 0

                # Mute
                mute_match = re.search(r"Mute: (\w+)", block)
                muted = mute_match and mute_match.group(1) == "yes"

                if muted:
                    return f" 🔇 {volume}% "
                elif volume == 0:
                    return f" 🔈 {volume}% "
                elif volume < 50:
                    return f" 🔉 {volume}% "
                elif volume < 100:
                    return f" 🔊 {volume}% "
                else:
                    return f" 🔊 100% "
        return "Sink not found"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(get_volume())
