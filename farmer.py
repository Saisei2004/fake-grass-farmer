from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path
import random


OUTPUT_FILE = Path("data/fake_grass.log")
JST = timezone(timedelta(hours=9))

MESSAGES = [
    "🌱 今日も健気に草が生えた。努力ではない。農業である。",
    "🌿 Fake Grass Farmer は静かに畑を耕した。",
    "🍀 今日の草は自動化によって合法的に発芽した。",
    "🌾 本日の貢献: 視覚的には存在する。",
    "🌵 草ではない何かもついでに生えた。",
    "🚜 農家は眠っていたが、畑は動いていた。",
    "🧑‍🌾 No work. No discipline. Just scheduled agriculture.",
    "🟩 Green pixels were cultivated successfully.",
    "🌱 Another fake contribution has sprouted.",
    "🌿 The field was updated by a very serious farmer.",
]


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    now_jst = now_utc.astimezone(JST)
    run_date = now_jst.date().isoformat()

    if OUTPUT_FILE.exists():
        text = OUTPUT_FILE.read_text(encoding="utf-8")
        if f"run_date={run_date} " in text:
            print(f"Fake Grass Farmer already succeeded for {run_date}.")
            return

    message = random.choice(MESSAGES)

    line = (
        f"run_date={run_date} "
        f"jst={now_jst.isoformat()} "
        f"utc={now_utc.isoformat()} "
        f"{message}\n"
    )

    with OUTPUT_FILE.open("a", encoding="utf-8") as file:
        file.write(line)

    print(f"Fake Grass Farmer wrote success record for {run_date}.")


if __name__ == "__main__":
    main()
