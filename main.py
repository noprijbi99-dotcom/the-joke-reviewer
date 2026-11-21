"""The joke the reviewer laughs at - make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, no trailing newline). Stdlib only, no network.
"""
import os

JOKE = ("I asked my agent to remove the dead code. It deleted the tests "
        "first — and for one perfect moment, everything passed.")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
