import argparse

from .main import pretty_print

parser = argparse.ArgumentParser(description="Pretty print HTML, XML, or JSON strings.")
parser.add_argument("string", help="a string of HTML, XML, or JSON")


def main():
    args = parser.parse_args()
    string = args.string
    pretty_print(string)
