#!/usr/bin/env python3

import math


def is_valid_float(text: str) -> bool:
    if text.count(".") > 1:
        return False
    coordinates = text.split(".")
    return (all(coordinate.isdigit() for coordinate in coordinates)
            and text != "" and text != ".")


def get_player_pos() -> tuple[float, float, float] | None:
    line = input("Enter new coordinates as floats in format 'x,y,z': ")
    coordinate = [p.strip() for p in line.split(",")]
    if len(coordinate) != 3:
        print("Invalid syntax")
        return None
    coordinates = []
    invalid: list[str] = []
    for p in coordinate:
        if is_valid_float(p):
            coordinates.append(float(p))
        else:
            invalid.append(p)
    if not coordinates or len(invalid) >= 2:
        quoted = [f"'{x}'" for x in invalid]
        print(f"Error on parameters {', '.join(quoted)}: could not convert"
              f" strings to float: {', '.join(quoted)}")
        return None
    if len(invalid) == 1:
        quoted = [f"'{x}'" for x in invalid]
        print(f"Error on parameter {', '.join(quoted)}: could not convert"
              f" string to float: {', '.join(quoted)}")
        return None
    return (coordinates[0], coordinates[1], coordinates[2])


def position_tracker() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_coordinates = None
    while first_coordinates is None:
        first_coordinates = get_player_pos()
    print(f"Got a first tuple: {first_coordinates}")
    print(f"It includes: X={first_coordinates[0]}, Y={first_coordinates[1]}, "
          f"Z={first_coordinates[2]}")
    x1 = first_coordinates[0]
    y1 = first_coordinates[1]
    z1 = first_coordinates[2]
    first_coordinates_distance = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance to center: {round(first_coordinates_distance, 4)}\n")
    print("Get a second set of coordinates")
    second_coordinates = None
    while second_coordinates is None:
        second_coordinates = get_player_pos()
    x2 = second_coordinates[0]
    y2 = second_coordinates[1]
    z2 = second_coordinates[2]
    twoset_coordinates_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2
                                            + (z2 - z1) ** 2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{abs(round(twoset_coordinates_distance, 4))}")


if __name__ == '__main__':
    position_tracker()
