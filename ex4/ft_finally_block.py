#!/usr/bin/python3


class PlantError(Exception):
    """Exception for invalid plant names."""
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def raise_plant_error() -> None:
    """Raise a PlantError with an invalid plant name message."""
    raise PlantError("Invalid plant name to water:")


def water_plant(plant_name: str) -> None:
    """Water a plant if its name is capitalized, raise PlantError otherwise."""
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    """Test watering system with valid and invalid plant names."""
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as err:
        print(f"Caught PlantError: {err}\n"
              ".. ending tests and return to main")
    finally:
        print("Closing watering System")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as err:
        print(f"Caught PlantError: {err}\n"
              ".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
