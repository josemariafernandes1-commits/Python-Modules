#!/usr/bin/env python3

import sys
import typing


def opening_file(filename: str) -> typing.IO:
    print(f"Accessing file '{filename}'")
    return open(filename)


def reading_file(filename: typing.IO[str]) -> None:
    print("---")
    print()
    print(filename.read())
    print("---")


def closing_file(filename: typing.IO[str]) -> None:
    filename.close()
    print(f"File '{filename.name}' closed.")


def system_check() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        sys.exit(1)
    print("=== Cyber Archives Recovery ===")
    try:
        opened_file = opening_file(sys.argv[1])
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}\n")
        sys.exit(1)
    except PermissionError as e:
        print(f"Error opening file {sys.argv[1]}: {e}\n")
        sys.exit(1)
    reading_file(opened_file)
    closing_file(opened_file)


if __name__ == '__main__':
    system_check()
