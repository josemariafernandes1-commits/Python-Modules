#!/usr/bin/env python3

import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    if len(sys.argv) > 1:
        # print(f"Arguments received: {len(sys.argv)}")
        # for i in range(1, len(sys.argv)):
        #     print(f"Argument {i}: {sys.argv[i]}")
        t = 1
        for arg in sys.argv[1:]:
            print(f"Argument {t}: {arg}")
            t += 1
        # for i, arg in enumerate(sys.argv[1:], start=1):
        #     print(f"Argument {i}: {arg}")
    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == '__main__':
    command_quest()
