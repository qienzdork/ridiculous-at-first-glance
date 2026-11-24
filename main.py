"""Ridiculous at First Glance, Real by the Second.

Entrypoint for the make.fun bounty
u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

Writes one original sentence (<= 200 characters) pitching a bizarre
startup idea that sounds absurd until the business logic lands, to the
path in env OUTPUT_PATH (default /output/entry.txt).
"""

import os

# The entry: one original sentence, written for this bounty.
ENTRY = (
    "We bottle the smell of rain and sell it to windowless offices, "
    "because workers who never see daylight will pay to pretend "
    "the weather still exists."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(os.path.abspath(output_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
