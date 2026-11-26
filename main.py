"""One-star alien tourist review of Earth — with a five-star food twist.

Writes the entry text to /output/entry.txt, deterministically, with no
trailing newline. Python standard library only.
"""

import os

ENTRY = "One star: Earth's gravity flattened my spine and its humans queue for absolutely everything, yet one plate of nasi goreng justified nine light-years — I'd crawl back for seconds."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
