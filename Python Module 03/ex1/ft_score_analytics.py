#!/usr/bin/env python3

import sys


def setup_scores(args: list[str]) -> list[int | float]:
    scoreboard: list[int | float] = []
    for arg in args:
        try:
            scoreboard.append(int(arg))
        except ValueError:
            try:
                value = float(arg)
                if value != value or abs(value) == float("inf"):
                    raise ValueError(f"Invalid parameter: '{value}'")
                elif "e" in arg.lower():
                    raise ValueError(f"Invalid parameter: '{value}'")
                scoreboard.append(float(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
    return scoreboard


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
