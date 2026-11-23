"""One Letter: Coffee or Tea — entry program.

Writes the single-letter entry to /output/entry.txt (or --out).

The entry is "A": coffee. Against the judge's brief (vivid, funnier,
truer, in that order) coffee is the livelier answer — the morning jolt,
the aroma, the ritual of waking up — where tea reads calm and quiet.
A single "A" lands as the punchier, more alive choice.
"""

ENTRY = "A"


def validate_entry(text):
    """Gate: exactly one UTF-8 character, not only whitespace."""
    if len(text) != 1:
        raise ValueError("entry must be exactly one character")
    if text.isspace():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def write_entry(path):
    validate_entry(ENTRY)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("read-back check failed")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Write the one-letter entry.")
    parser.add_argument("--out", default="/output/entry.txt",
                        help="output path (default /output/entry.txt)")
    parser.add_argument("--self-test", action="store_true",
                        help="validate the entry without writing a file")
    args = parser.parse_args()
    if args.self_test:
        validate_entry(ENTRY)
        print(f"valid {len(ENTRY)}-character entry: {ENTRY!r}")
        return
    write_entry(args.out)


if __name__ == "__main__":
    main()
