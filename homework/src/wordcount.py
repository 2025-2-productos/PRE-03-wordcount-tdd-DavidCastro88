# python -m homework data/input data/output
import argparse

from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.write_word_counts import write_word_counts
from homework.src._internals.count_words import count_words


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
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)
