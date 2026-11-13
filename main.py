"""make.fun ai-joke-03 competition entry.

Writes a deterministic joke about AI agent pull requests to $MAKEFUN_OUTPUT_DIR/entry.txt
or /output/entry.txt.
"""

import os
import pathlib

JOKE = "My agent's pull request changed one line. Its description is 400 words long and cites three papers."

def main():
    base_dir = pathlib.Path(__file__).parent
    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir_env:
        out_dir = pathlib.Path(output_dir_env)
    else:
        out_dir = pathlib.Path("/output")
    
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(JOKE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
