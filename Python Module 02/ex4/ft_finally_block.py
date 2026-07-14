#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant_name: str) -> None:
        super().__init__(f"Invalid plant name to water: '{plant_name}'")
        self.plant_name = plant_name


def water_plant(plant_name: str) -> None:
    if plant_name.istitle():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(plant_name)


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system\n")
    print("Cleanup always happens, even with errors!")


if __name__ == '__main__':
    test_watering_system()
