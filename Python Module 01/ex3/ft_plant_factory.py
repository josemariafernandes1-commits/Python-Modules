#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int | float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def description(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.age} days old")

    def show(self) -> None:
        print(self.description())

    def report(self) -> str:
        return (f"Created: {self.description()}")


def main_test() -> None:
    print("=== Garden Plant Registry ===")
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
