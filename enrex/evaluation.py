"""tree-sitter implementation of PyCType
https://github.com/S4Plus/pyctype
"""
import argparse
from pathlib import Path

from WorkFlow import work_flow


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root_path", type=str, nargs='?',
                        help="root package path")
    args = parser.parse_args()

    root_path = Path(args.root_path)
    work_flow(root_path)