#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int | float, age: int) -> None:
        self.plant_name = name
        self.plant_height = height
        self.plant_age = age
        self.plant_name = self.plant_name.lower()
        self.plant_name = self.plant_name.capitalize()

    def show(self) -> None:
        print(f"{self.plant_name}: {self.plant_height:.1f}cm, {self.plant_age}"
              f" days old")

    def grow(self, height: int | float) -> None:
        self.plant_height += round(height, 1)

    def age(self, age: int) -> None:
        self.plant_age += age


def growth_report() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("rosE", 25.0, 30)
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age(1)
        rose.show()
    print(f"Growth this week: {round(day * 0.8, 1)}cm")


if __name__ == '__main__':
    growth_report()
