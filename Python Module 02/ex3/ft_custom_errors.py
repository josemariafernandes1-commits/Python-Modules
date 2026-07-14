#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant_name: str, plant_status: str) -> None:
        super().__init__(f"The {plant_name} plant is {plant_status}!")
        self.plant_name = plant_name
        self.plant_status = plant_status


class WaterError(GardenError):
    def __init__(self, water_level: int | float, water_minimum: int | float,
                 plant_container: str) -> None:
        super().__init__(f"Not enough water in the {plant_container}!")
        self.water_level = water_level
        self.water_minimum = water_minimum
        self.plant_container = plant_container


def check_plant(plant_name: str, plant_status: str) -> None:
    if plant_status != "healthy":
        raise PlantError(plant_name, plant_status)


def check_water_level(water_level: int | float, water_minimum: int | float,
                      plant_container: str) -> None:
    if water_level < water_minimum:
        raise WaterError(water_level, water_minimum, plant_container)


def custom_class_errors_test() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        check_plant("tomato", "wilting")
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
    print()
    print("Testing WaterError...")
    try:
        check_water_level(5, 7, "tank")
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", "wilting")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_level(5, 7, "tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == '__main__':
    custom_class_errors_test()
