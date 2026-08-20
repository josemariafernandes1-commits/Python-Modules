#!/usr/bin/env python3

import sys


def setup_scores(args: list[str]) -> list[int]:
    scoreboard = []
    for arg in sys.argv[1:]:
        if arg.isdigit():
            scoreboard.append(int(arg))
        else:
            print(f"Invalid parameter: '{arg}'")
    return (scoreboard)


def score_cruncher() -> None:
    print("=== Player Score Analytics ===")
    print(f"Program name: {sys.argv[0]}")
    scoreboard = setup_scores(sys.argv[1:])
    if len(sys.argv) == 1 or not scoreboard:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...\n")
        return
    print(f"Scores processed: {scoreboard}")
    print(f"Total players: {len(scoreboard)}")
    print(f"Total score: {sum(scoreboard)}")
    print(f"Average score: {sum(scoreboard) / len(scoreboard)}")
    print(f"High score: {max(scoreboard)}")
    print(f"Low score: {min(scoreboard)}")
    print(f"Score range: {max(scoreboard) - min(scoreboard)}\n")


if __name__ == '__main__':
    score_cruncher()
