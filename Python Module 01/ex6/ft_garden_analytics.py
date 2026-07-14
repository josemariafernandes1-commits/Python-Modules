#!/usr/bin/env python3

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._rec_grow = 0
            self._rec_age = 0
            self._rec_show = 0

        def record_grow(self) -> None:
            self._rec_grow += 1

        def record_age(self) -> None:
            self._rec_age += 1

        def record_show(self) -> None:
            self._rec_show += 1

        def stats_display(self) -> None:
            print(self.general_description())

        def general_description(self) -> str:
            return (f"Stats: {self._rec_grow} grow, {self._rec_age} age, "
                    f"{self._rec_show} show")

    def show_stats(self) -> None:
        print(f"[statistics for {self._plant_name}]")
        self._stats.stats_display()

    def __init__(self, name: str, height: int | float, age: int) -> None:
        self._stats = Plant.Statistics()
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
        return (f"{self._plant_name}: {self._plant_height}cm, "
                f"{self._plant_age} days old")

    def show(self) -> None:
        self._stats.record_show()
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
        print(f"Height updated: {self._plant_height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._plant_name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._plant_age = age
        print(f"Age updated: {self._plant_age} days")

    def get_height(self) -> float:
        return self._plant_height

    def get_age(self) -> float:
        return self._plant_age

    @classmethod
    def anonymous_create(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def is_valid_age(age: int) -> bool:
        return age > 365


def general_show(plant: Plant) -> None:
    plant.show_stats()


class Flower(Plant):
    _header_shown = False

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False
        # self.create_report()

    def full_bloom(self, growth: int) -> None:
        print(f"[asking the {self._plant_name.lower()} to grow and bloom]")
        self._blooming = True
        self.grow(growth)
        self._stats.record_grow()

    # def create_report(self) -> None:
    #     status = ("is blooming beautifully!" if self._blooming
    #               else "has not bloomed yet")
    #     print(f"Plant created: {super().description()}\n"
    #           f" Color: {self._color}\n"
    #           f" {self._plant_name} {status}")

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

    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._rec_shade = 0

        def record_shade(self) -> None:
            self._rec_shade += 1

        def general_description(self) -> str:
            return (f"{super().general_description()}\n"
                    f" {self._rec_shade} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats: "Tree.TreeStatistics" = Tree.TreeStatistics()
        # self.create_report()

    def shade(self) -> None:
        print(f"[asking the {self._plant_name.lower()} to produce shade]")
        self._stats.record_shade()
        print(f"Tree {self._plant_name} now produces a shade of "
              f"{self._plant_height}"
              f"cm long and {self._trunk_diameter}cm wide.")

    # def create_report(self) -> None:
    #     print(f"Plant created: {super().description()}\n"
    #           f" Trunk diameter: {self._trunk_diameter}cm")

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
        # self.create_report()

    def grow_and_age(self, age: int, height: int | float) -> None:
        print(f"[make {self._plant_name.lower()} grow and age for {age} days]")
        self.grow((height))
        self.age(age)
        self._nutritional_value += age
        self._stats.record_grow()
        self._stats.record_age()

    # def create_report(self) -> None:
    #     print(f"Plant created: {super().description()}\n"
    #           f" Harvest season: {self._harvest_season}\n"
    #           f" Nutritional value: {self._nutritional_value}")

    def description(self) -> str:
        return (f"{super().description()}\n"
                f" Harvest season: {self._harvest_season}\n"
                f" Nutritional value: {self._nutritional_value}")

    def show(self) -> None:
        if not Vegetable._header_shown:
            print("=== Vegetable")
            Vegetable._header_shown = True
        super().show()


class Seed(Flower):
    _header_shown = False

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed = int(0)
        self._blooming = False
        # self.create_report()

    def germinate(self, height: int | float, age: int, seed: int) -> None:
        print(f"[make {self._plant_name.lower()} grow, age and bloom]")
        self._blooming = True
        self.grow(height)
        self._stats.record_grow()
        self.age(age)
        self._stats.record_age()
        self._seed += seed

    def description(self) -> str:
        return (f"{super().description()}\n"
                f" Seeds: {self._seed}")

    # def create_report(self) -> None:
    #     print(f"Plant created: {super().description()}\n"
    #           f" Seeds: {self._seed}")

    def show(self) -> None:
        if not Seed._header_shown:
            print("=== Seed")
            Seed._header_shown = True
        super().show()


def main_test() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_valid_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_valid_age(400)}")
    print("")
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    rose.show()
    general_show(rose)
    rose.full_bloom(8)
    rose.show()
    general_show(rose)
    print()
    oak.show()
    general_show(oak)
    oak.shade()
    general_show(oak)
    print()
    sunflower.show()
    sunflower.germinate(30, 20, 42)
    sunflower.show()
    general_show(sunflower)
    print()
    print("=== Anonymous")
    unknown = Plant.anonymous_create()
    unknown.show()
    general_show(unknown)


if __name__ == '__main__':
    main_test()
