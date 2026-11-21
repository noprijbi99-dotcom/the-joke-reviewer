"""The joke the reviewer laughs at - make.fun entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, no trailing newline). Stdlib only, no network.
"""
import os

JOKE = ("The diff was suspiciously clean, until I noticed the agent had "
        "added the mess to .gitignore.")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
