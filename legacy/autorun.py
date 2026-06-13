from __future__ import annotations

import re
import subprocess
import time
from pathlib import Path
from datetime import datetime, timedelta


ROOT_DIR = Path(__file__).resolve().parent
SLEEP_FILE = ROOT_DIR / "sleep.md"


def read_sleep_seconds() -> int:
    text = SLEEP_FILE.read_text(encoding="utf-8")
    match = re.search(r"\b(\d+)\b", text)
    if not match:
        raise ValueError(f"No sleep value found in {SLEEP_FILE}")
    return int(match.group(1))


def main() -> None:
    while True:
        subprocess.run(["opencode", "run", "Play!"], check=False)

        sleep_seconds = read_sleep_seconds()
        wake_time = datetime.now() + timedelta(seconds=sleep_seconds)

        print(f"[AGENT] Sleeping for {sleep_seconds}s until {wake_time.isoformat()}")

        time.sleep(sleep_seconds)


if __name__ == "__main__":
    main()
