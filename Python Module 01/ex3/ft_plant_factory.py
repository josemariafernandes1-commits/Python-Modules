#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int | float, age: int) -> None:
        self.plant_name = name
        self.plant_height = height
        self.plant_age = age

    def description(self) -> str:
        return (f"{self.plant_name}: {self.plant_height}cm, {self.plant_age}"
                f" days old")

    def show(self) -> None:
        print(self.description())

    def report(self) -> str:
        return (f"Created: {self.description()}")

    def grow(self, height: int | float) -> None:
        self.height = round(height)

    def age(self, age: int) -> None:
        self.plant_age = age


def main_test() -> None:
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    for plant in plants:
        print(plant.report())


if __name__ == '__main__':
    main_test()
