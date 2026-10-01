#!/usr/bin/env python3

import random


def gen_player_list() -> list[str]:
    player_names = sorted({'Alice', 'Bob', 'Charlie', 'Dylan', 'Emma',
                           'Gregory', 'John', 'Kevin', 'Liam'})
    list_randomized = []
    for name in player_names:
        if random.choice([True, False]):
            list_randomized.append(name.capitalize())
        else:
            list_randomized.append(name.lower())
    return list_randomized


def gen_player_scores(players: list[str]) -> dict[str, int]:
    player_scores: dict[str, int] = {player: random.randint(1, 1000)
                                     for player in players}
    return player_scores


def player_lists_displayed() -> None:
    names = gen_player_list()
    capitalized_list = [name.capitalize() for name in names]
    capitalized_names = [name for name in names if name[0].isupper()]
    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {capitalized_list}")
    print(f"New list of capitalized names only: {capitalized_names}\n")
    player_scoreboard = gen_player_scores(capitalized_list)
    print(f"Score dict: {player_scoreboard}")
    average = round(sum(player_scoreboard.values())
                    / len(player_scoreboard), 2)
    print(f"Score average is {average}")
    top_scores = {}
    for name, score in player_scoreboard.items():
        if score > average:
            top_scores[name] = score
    print(f"High scores: {top_scores}")


if __name__ == '__main__':
    player_lists_displayed()
