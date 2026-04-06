#!/usr/bin/python3


def garden_operations(operation_number: int) -> None:
    """Perform faulty garden operations based on operation number (0-3)."""
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/excistent/file")
    elif operation_number == 3:
        "string" + 1


def test_error_types() -> None:
    """Test all error types and catching each exception."""
    for num in range(0, 5):
        print(f"Testing operation {num}...")
        try:
            garden_operations(num)
            print("Operation completed successfully")
        except ValueError as err:
            print(f"Caught ValueError: {err}")
        except ZeroDivisionError as err:
            print(f"Caught ZeroDivisionError: {err}")
        except FileNotFoundError as err:
            print(f"Caught FileNotFoundError: {err}")
        except TypeError as err:
            print(f"Caught TypeError: {err}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print()
    print("All error types tested successfully!")
