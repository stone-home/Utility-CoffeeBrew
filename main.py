#!/usr/bin/env python3
import argparse
from src.bean2obsidian import Bean2Obsidian


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Beanconqueror JSON to Obsidian notes."
    )
    parser.add_argument("json_file", help="Path to the Beanconqueror JSON file.")
    parser.add_argument(
        "output_dir", help="Path to the output directory for Obsidian notes."
    )
    parser.add_argument(
        "-b",
        "--bc_folder",
        default=None,
        help="Path to the folder containing the Beanconqueror JSON file and images.",
    )
    args = parser.parse_args()

    obsidian = Bean2Obsidian(args.json_file, args.output_dir)
    obsidian.save()
