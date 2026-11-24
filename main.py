"""Write the one-word Wi-Fi entry to entry.txt.

The word is the Wi-Fi's own signature lie: full bars, "Connected",
nothing loading — it gaslights you.
"""

import os

WORD = "Gaslighting"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
