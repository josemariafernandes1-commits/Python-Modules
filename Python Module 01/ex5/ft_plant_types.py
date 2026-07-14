#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int | float, age: int) -> None:
        self._plant_name = name
        if (height < 0):
            self._plant_height = 0.0
            print(f"{self._plant_name}: Error, height can't be negative")
            print("Defaulted to 0")
        else:
            self._plant_height = height
        if (age < 0):
            self._plant_age = 0
            print(f"{self._plant_name}: Error, age can't be negative")
            print("Defaulted to 0")
        else:
            self._plant_age = age

    def description(self) -> str:
        return (f"{self._plant_name}: {self._plant_height}cm,"
                f" {self._plant_age} days old")

    def show(self) -> None:
        print(self.description())

    def report(self) -> str:
        return (f"Plant created: {self.description()}")

    def grow(self, height: int | float) -> None:
        self._plant_height += round(height, 1)

    def age(self, age: int) -> None:
        self._plant_age += age

    def set_height(self, height: int | float) -> None:
        if height < 0:
            print(f"{self._plant_name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._plant_height = height
        # print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._plant_name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._plant_age = age
        # print(f"Age updated: {self._age} days")

    def get_height(self) -> int | float:
        return self._plant_height

    def get_age(self) -> int:
        return self._plant_age


class Flower(Plant):
    _header_shown = False

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False

    def bloom(self) -> None:
        print(f"[asking the {self._plant_name} to bloom]")
        self._blooming = True

    def description(self) -> str:
        status = ("is blooming beautifully!" if self._blooming
                  else "has not bloomed yet")
        return (f"{super().description()}\n"
                f" Color: {self._color}\n"
                f" {self._plant_name} {status}")

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

    def produce_shade(self) -> None:
        print(f"[asking the {self._plant_name} to produce shade]")
        print(f"Tree {self._plant_name} now produces a shade of "
              f"{self._plant_height}cm"
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

    def grow_and_age(self, age: int, height: int | float) -> None:
        print(f"[make {self._plant_name.lower()} grow and age for {age} days]")
        self.age(age)
        self.grow((height))
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
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    rose.show()
    rose.bloom()
    rose.show()
    print("")
    oak.show()
    oak.produce_shade()
    print("")
    tomato.show()
    tomato.grow_and_age(20, 42.0)
    tomato.show()


if __name__ == '__main__':
    main_test()
