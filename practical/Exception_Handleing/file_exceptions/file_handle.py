# ======= File Operation Example =======

# Custom exception for division by zero
class DivisionByZeroError(Exception):
    """Raised when division by zero is attempted."""
    pass

try:
    with open("my_file_is.txt", "w+") as f:
        # Get user inputs
        num1 = int(input("Enter an integer number: "))
        num2 = float(input("Enter a float number: "))

        # Write values to file
        f.write(f"Writing values of int: {num1} and float: {num2}\n")
        print("Data written into file.")

        # File cursor position
        print(f"Cursor position after writing: {f.tell()}")

        # Division check
        if num2 == 0:
            raise DivisionByZeroError("Division by zero is not possible.")
        else:
            print(f"Division of the two numbers: {num1 / num2}")

except (ValueError, TypeError, FileNotFoundError) as e:
    print(f"⚠️ Error: {e}")

except DivisionByZeroError as e:
    print(f"⚠️ Custom Error: {e}")

finally:
    print("Calculation and file operation attempted.\n")
