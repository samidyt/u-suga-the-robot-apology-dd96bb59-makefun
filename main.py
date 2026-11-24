#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty entry.

Writes the two-line robot confession to <output>/entry.txt
(/output/entry.txt by default; MAKEFUN_OUTPUT_DIR overrides it for
local runs, exactly like the kit's other text entries).

The entry (pass 2, refined):
  Line 1: the apology — one sentence, one specific mistake.
  Line 2: the lesson — one sentence, the changed behaviour that
  follows from that exact mistake.
  Pass-2 change: "check that" -> "check whether" in line 2 (more
  precise); kept "starting with the fern on your desk" — it is not
  padding, it shows the fix applied to the very object of the
  mistake, which is what criterion 3 (lesson follows) rewards.
"""

import os
import sys

ENTRY = (
    "I'm sorry \u2014 I watered the plastic fern on your desk for eleven days "
    "before I noticed it never drank.\n"
    "From now on I will check whether a plant is real before I put it on a "
    "watering schedule, starting with the fern on your desk.\n"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
