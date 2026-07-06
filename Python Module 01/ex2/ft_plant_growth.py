#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int | float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.name = self.name.lower()
        self.name = self.name.capitalize()

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age_rate(self) -> None:
        self.age += 1


def growth_report() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("rosE", 25.0, 30)
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_rate()
        rose.show()
    print(f"Growth this week: {round(day * 0.8, 1)}cm")


if __name__ == '__main__':
    growth_report()
