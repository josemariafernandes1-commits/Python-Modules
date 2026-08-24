#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: set[str]) -> set[str]:
    size_list = random.randint(1, len(achievements))
    return set(random.sample(list(achievements), size_list))


def list_player_achievements() -> None:
    print("=== Achievement Tracker System ===\n")
    achiev_list = {'Strategist', 'Speed Runner', 'Survivor',
                   'Master Explorer', 'Treasure Hunter', 'First Steps',
                   'Collector Supreme', 'Untouchable', 'Sharp Mind',
                   'Crafting Genius', 'World Savior', 'Hidden Path Finder',
                   'Unstoppable', 'Boss Slayer'}
    Alice = gen_player_achievements(achiev_list)
    Bob = gen_player_achievements(achiev_list)
    Charlie = gen_player_achievements(achiev_list)
    Dylan = gen_player_achievements(achiev_list)
    print(f"Player Alice: {(Alice)}")
    print(f"Player Bob: {(Bob)}")
    print(f"Player Charlie: {(Charlie)}")
    print(f"Player Dylan: {(Dylan)}")
    print()
    print(f"All distinct achievements: "
          f"{Alice.difference(Bob, Charlie, Dylan)}\n")
    print(f"Common achievements: "
          f"{set.intersection(Alice, Bob, Charlie, Dylan)}\n")
    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Alice, Bob, Charlie)}")
    print()
    print(f"Alice is missing: "
          f"{set.union(Bob, Charlie, Dylan).difference(Alice)}")
    print(f"Bob is missing: "
          f"{set.union(Alice, Charlie, Dylan).difference(Bob)}")
    print(f"Charlie is missing: "
          f"{set.union(Alice, Bob, Dylan).difference(Charlie)}")
    print(f"Dylan is missing: "
          f"{set.union(Alice, Bob, Charlie).difference(Dylan)}")


if __name__ == '__main__':
    list_player_achievements()
