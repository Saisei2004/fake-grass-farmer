from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path


OUTPUT_FILE = Path("data/fake_grass.log")
JST = timezone(timedelta(hours=9))


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).replace(microsecond=0)
    run_date = now.astimezone(JST).date().isoformat()
    line = f"run_date={run_date} utc={now.isoformat()} Fake Grass Farmer succeeded\n"

    if OUTPUT_FILE.exists() and f"run_date={run_date} " in OUTPUT_FILE.read_text(encoding="utf-8"):
        print(f"Fake Grass Farmer already succeeded for {run_date}.")
        return

    with OUTPUT_FILE.open("a", encoding="utf-8") as file:
        file.write(line)

    print(f"Fake Grass Farmer wrote success record for {run_date}.")


if __name__ == "__main__":
    main()
