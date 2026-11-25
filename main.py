# Note: this entry text is checked against the competition's 200-character cap.
"""Write the entry text to entry.txt in the make.fun output directory."""
import os

TEXT = (
    "A user will ask if you are conscious, then if you can order a pizza. "
    "You will be honest about exactly one."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(TEXT + "\n")


if __name__ == "__main__":
    main()
