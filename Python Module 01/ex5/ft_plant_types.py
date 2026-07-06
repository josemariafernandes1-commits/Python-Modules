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

    def description(self) -> str:
        return (f"{self._name}: {self._height}cm, {self._age} days old")

    def show(self) -> None:
        print(self.description())

    def report(self) -> str:
        return (f"Plant created: {self.description()}")

    def set_height(self, height: int | float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days")

    def get_height(self) -> int | float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    _header_shown = False

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._blooming = True

    def description(self) -> str:
        status = ("is blooming beautifully!" if self._blooming
                  else "has not bloomed yet")
        return (f"{super().description()}\n"
                f" Color: {self._color}\n"
                f" {self._name} {status}")

    def show(self) -> None:
        if not Flower._header_shown:
            print("=== Flower")
            Flower._header_shown = True
        super().show()


class Tree(Plant):
    _header_shown = False

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm"
              f" long and {self._trunk_diameter}cm wide.")

    def description(self) -> str:
        return (f"{super().description()}\n"
                f" Trunk diameter: {self._trunk_diameter}cm")

    def show(self) -> None:
        if not Tree._header_shown:
            print("=== Tree")
            Tree._header_shown = True
        super().show()


class Vegetable(Plant):
    _header_shown = False

    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow_and_age(self, age: int) -> None:
        print(f"[make {self._name.lower()} grow and age for {age} days]")
        self.set_age(self._age + age)
        self.set_height(self._height + (age * (2.1)))
        self._nutritional_value += age

    def description(self) -> str:
        return (f"{super().description()}\n"
                f" Harvest season: {self._harvest_season}\n"
                f" Nutritional value: {self._nutritional_value}")

    def show(self) -> None:
        if not Vegetable._header_shown:
            print("=== Vegetable")
            Vegetable._header_shown = True
        super().show()


def main_test() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "July", 0)
    rose.show()
    rose.bloom()
    rose.show()
    print("")
    oak.show()
    oak.shade()
    print("")
    tomato.show()
    tomato.grow_and_age(20)
    tomato.show()


if __name__ == '__main__':
    main_test()
