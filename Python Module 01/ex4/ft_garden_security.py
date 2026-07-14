#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int | float, age: int) -> None:
        self._name = name
        if (height < 0):
            self._height = 0.0
            print(f"{self._name}: Error, height can't be negative")
            print("Defaulted to 0")
        else:
            self._height = height
        if (age < 0):
            self._age = 0
            print(f"{self._name}: Error, age can't be negative")
            print("Defaulted to 0")
        else:
            self._age = age
        self.create_report()

    def description(self) -> str:
        return (f"{self._name}: {self._height}cm, {self._age} days old")

    def show(self) -> None:
        print(self.description())

    def create_report(self) -> None:
        print(f"Plant created: {self.description()}")

    def report(self) -> str:
        return (f"Current state: {self.description()}")

    def set_height(self, height: int | float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {round(self._height)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def get_height(self, height: int | float) -> int | float:
        return self._height

    def get_age(self, age: int) -> int:
        return self._age


def main_test() -> None:
    print("=== Garden Security System ===")
    # plants = [
    #     Plant("Rose", 15.0, 10),
    #     Plant("Oak", 200.0, 365),
    #     Plant("Cactus", 5.0, 90),
    #     Plant("Sunflower", 80.0, 45),
    #     Plant("Fern", 15.0, 120)
    # ]
    rose = Plant("Rose", 15.0, 10)
    print("")
    rose.set_height(25.0)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    rose.set_age(-5)
    print("")
    print(rose.report())


if __name__ == '__main__':
    main_test()
