#!/usr/bin/env python3

import sys


def inventory_insertion(input: list[str]) -> dict[str, int]:
    backpack: dict[str, int] = {}
    for arg in input:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if not parts[1].isdigit():
            print(f"Quantity error for '{parts[0]}': invalid literal for "
                  f"int() with base 10: '{parts[1]}'")
            continue
        name, quantity = parts
        if name in backpack:
            print(f"Redundant item '{arg}' - discarding")
            continue
        backpack[name] = int(quantity)
    return (backpack)


def value_item(backpack: dict[str, int],
               high_or_low: int) -> tuple[str, int]:
    if (high_or_low == 1):
        return_value = -1
    elif (high_or_low == 0):
        return_value = sum(backpack.values())
    for name, quantity in backpack.items():
        if quantity > return_value and high_or_low == 1:
            return_item = name
            return_value = quantity
        elif quantity < return_value and high_or_low == 0:
            return_item = name
            return_value = quantity
    return return_item, return_value


def inventory_sorting() -> None:
    print("=== Inventory System Analysis ===")
    backpack = inventory_insertion(sys.argv[1:])
    items = list(backpack.keys())
    print(f"Got inventory: {backpack}")
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(backpack)} "
          f"items: {sum(backpack.values())}")
    for name, quantity in backpack.items():
        print(f"Item {name} represents "
              f"{round(quantity/sum(backpack.values())*100, 1)}%")
    top_item, top_value = value_item(backpack, 1)
    least_item, least_value = value_item(backpack, 0)
    print(f"Item most abundant: {top_item} with quantity {top_value}")
    print(f"Item least abundant: {least_item} with quantity {least_value}")
    amulet_appears = {"magic_item": 1}
    backpack.update(amulet_appears)
    print(f"Updated inventory: {backpack}")


if __name__ == '__main__':
    inventory_sorting()
