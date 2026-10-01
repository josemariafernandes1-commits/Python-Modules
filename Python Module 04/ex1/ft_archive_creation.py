#!/usr/bin/env python3

import sys
import typing


def opening_file(filename: str) -> typing.IO:
    print(f"Accessing file '{filename}'")
    return open(filename)


def read_change_file(filename: typing.IO[str]) -> str:
    print("---")
    print()
    original = filename.read()
    print(original)
    print("---")
    content = ""
    for char in original:
        if char == '\n':
            content += '#' + char
        else:
            content += char
    return content


def closing_file(filename: typing.IO[str]) -> None:
    filename.close()
    print(f"File '{filename.name}' closed.\n")


def system_data_manipulation() -> None:
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
    manipulated_file = read_change_file(opened_file)
    closing_file(opened_file)
    print("Transform data:")
    print("---")
    print()
    print(manipulated_file)
    print("---")
    copying_content(manipulated_file)


def copying_content(file_content: str) -> None:
    save_filename = input("Enter new file name (or empty):")
    if save_filename:
        print(f"Saving data to '{save_filename}'")
        saved_file = open(save_filename, 'w')
        saved_file.write(file_content)
        saved_file.close()
        print(f"Data saved in file '{save_filename}'")
    else:
        print("Not saving data.")


if __name__ == '__main__':
    system_data_manipulation()
