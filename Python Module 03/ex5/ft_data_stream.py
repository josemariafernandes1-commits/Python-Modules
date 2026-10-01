#!/usr/bin/env python3

import typing
import random


def gen_event(players: list[str], actions:
              list[str]) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def generator_display() -> None:
    print("=== Game Data Stream Processor ===")
    player_list = ['alice', 'bob', 'charlie', 'dylan']
    action_list = ['run', 'eat', 'sleep', 'grab',
                   'move', 'climb', 'swim', 'release']
    event = gen_event(player_list, action_list)
    for i in range(1000):
        narrate = next(event)
        print(f"Event {i}: Player {narrate[0]} did action {narrate[1]}")
        # if i < 15 or i > 991:
        #     print(f"Event {i}: Player {narrate[0]} did action {narrate[1]}")
        # elif i == 15:
        #     print("(...)")
    sample_events = []
    for j in range(10):
        sample_events.append(next(event))
    print(f"Built list of 10 events: {sample_events}")
    for selected_event in consume_event(sample_events):
        print(f"Got event from list: {selected_event}")
        print(f"Remains in list: {sample_events}")


def consume_event(events: list
                  [tuple[str, str]]) -> typing.Generator[tuple[str, str],
                                                         None, None]:
    while events:
        chosen = random.randrange(len(events))
        yield events.pop(chosen)


if __name__ == '__main__':
    generator_display()
