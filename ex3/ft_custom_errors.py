#!/usr/bin/python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_error() -> None:
    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as err:
        print(f"Caught PlantError: {err}")
    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as err:
        print(f"Caught WaterError: {err}")
    print("\nTesting catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as err:
        print(f"Caught GardenError: {err}")
    try:
        raise_water_error()
    except GardenError as err:
        print(f"Caught GardenError: {err}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_error()
    print("\nAll custom error types work correctly!")
