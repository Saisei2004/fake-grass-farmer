from __future__ import annotations

import argparse
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


def pick_commit_count() -> int:
    return random.randint(0, 6)


def write_grass_entry(entry_index: int, entry_total: int) -> str:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    now_utc = datetime.now(timezone.utc).replace(microsecond=0)
    now_jst = now_utc.astimezone(JST)
    run_date = now_jst.date().isoformat()

    message = random.choice(MESSAGES)

    line = (
        f"run_date={run_date} "
        f"entry={entry_index}/{entry_total} "
        f"jst={now_jst.isoformat()} "
        f"utc={now_utc.isoformat()} "
        f"{message}\n"
    )

    with OUTPUT_FILE.open("a", encoding="utf-8") as file:
        file.write(line)

    return run_date


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Grow fake GitHub grass.")
    parser.add_argument("--count", action="store_true", help="Print a random commit count from 0 to 6.")
    parser.add_argument("--entry-index", type=int, default=1, help="Current grass entry number.")
    parser.add_argument("--entry-total", type=int, default=1, help="Total grass entries for this run.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.count:
        print(pick_commit_count())
        return

    run_date = write_grass_entry(args.entry_index, args.entry_total)
    print(
        "Fake Grass Farmer wrote success record "
        f"{args.entry_index}/{args.entry_total} for {run_date}."
    )


if __name__ == "__main__":
    main()
