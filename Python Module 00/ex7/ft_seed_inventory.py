def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.lower()
    unit = unit.lower()
    if unit == "packets":
        seed_type = seed_type.capitalize()
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "grams":
        seed_type = seed_type.capitalize()
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif unit == "area":
        seed_type = seed_type.capitalize()
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")


# if __name__ == "__main__":
#     ft_seed_inventory("tomato", 15, "Packets")
#     ft_seed_inventory("carrot", 8, "grams")
#     ft_seed_inventory("lettuce", 12, "area")
#     ft_seed_inventory("peas", 12, "area")
#     ft_seed_inventory("oranges", "two", "area")
#     ft_seed_inventory("lettuce", 7, "volume")
#     ft_seed_inventory("strawberries", 7, "unknown")
