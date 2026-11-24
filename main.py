"""Write the one-word Wi-Fi entry to entry.txt.

The word is the Wi-Fi's own bluff: a full house of bars, an empty hand —
it shows you five bars, then folds the moment you actually need it.
"""

import os

WORD = "Bluff"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
