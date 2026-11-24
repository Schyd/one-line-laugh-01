"""One-Line Laugh entry: write a single funny line to /output/entry.txt."""

import os

LINE = (
    "The Wi-Fi went down for ten minutes and my family finally talked to "
    "each other; we all agreed it was the worst ten minutes of the week."
)


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise ValueError(f"entry must be 1-200 non-whitespace chars, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
