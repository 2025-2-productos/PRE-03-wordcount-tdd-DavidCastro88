# python -m homework data/input data/output
import argparse
import sys

from homework.src._internals.read_all_lines import read_all_lines


def parse_args():

    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", help="Path to the input folder containing files to process.", type=str
    )
    parser.add_argument(
        "output", help="Path to the ouput folder containing files to process.", type=str
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


def main():
    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
