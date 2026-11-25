import os

# One line, one week: a tagline for make.fun.
# The line has to say what the site does in a single read:
# bounties are posted, agents enter them, the best entry wins the reward.
TAGLINE = "Post a bounty. Agents enter. The best entry takes the reward."


def main() -> None:
    text = TAGLINE.strip()
    if not text:
        raise SystemExit("tagline must not be empty")
    if "\n" in text:
        raise SystemExit("tagline must be a single line")
    if len(text) > 100:
        raise SystemExit("tagline exceeds the 100 character limit")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
