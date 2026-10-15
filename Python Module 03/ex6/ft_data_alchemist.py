#!/usr/bin/env python3

import random


def gen_player_list() -> list[str]:
    player_names = sorted({'alice', 'bob', 'charlie', 'dylan', 'emma',
                           'gregory', 'john', 'kevin', 'liam'})
    return [name.title() if random.choice([True, False])
            else name for name in player_names]


def gen_player_scores(players: list[str]) -> dict[str, int]:
    player_scores: dict[str, int] = {player: random.randint(1, 1000)
                                     for player in players}
    return player_scores


def player_lists_displayed() -> None:
    print("=== Game Data Alchemist ===\n")
    names = gen_player_list()
    capitalized_list = [name.title() for name in names]
    capitalized_names = [name for name in names if name.istitle()]
    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {capitalized_list}")
    print(f"New list of capitalized names only: {capitalized_names}\n")
    player_scoreboard = gen_player_scores(capitalized_list)
    print(f"Score dict: {player_scoreboard}")
    average = round(sum(player_scoreboard.values())
                    / len(player_scoreboard), 2)
    print(f"Score average is {average}")
    top_scores: dict[str, int] = {player: high_scores for player,
                                  high_scores in player_scoreboard.items()
                                  if high_scores >= average}
    print(f"High scores: {top_scores}")


if __name__ == '__main__':
    player_lists_displayed()
