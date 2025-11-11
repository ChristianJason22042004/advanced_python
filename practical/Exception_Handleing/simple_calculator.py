# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid
# input).
# Write a Python program to demonstrate handling multiple exceptions.

class MyCalc:
    def __init__(self):
        print("Welcome to MyCalc!\n")

    def my_calculator(self, input_1, input_2, operator):
        """
        Perform basic arithmetic operations (+, -, *, /, %) with exception handling.
        Returns a formatted string or error message.
        """
        try:
            # Validate input types
            if not isinstance(input_1, (int, float)) or not isinstance(input_2, (int, float)):
                raise TypeError("Inputs must be numbers")

            # Check for division by zero
            if operator == "/" and input_2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed")

            # Perform arithmetic operations
            if operator == "+":
                return f"Sum: {input_1 + input_2}"
            elif operator == "-":
                return f"Difference: {input_1 - input_2}"
            elif operator == "*":
                return f"Product: {input_1 * input_2}"
            elif operator == "/":
                return f"Division: {input_1 / input_2}"
            elif operator == "%":
                return f"Remainder: {input_1 % input_2}"
            else:
                raise ValueError(
                    "Invalid operator entered. Use +, -, *, /, or %")

        except (TypeError, ZeroDivisionError, ValueError) as e:
            return f"⚠️ Error: {e}"

        finally:
            # Always runs
            print("Calculation attempted.\n")


# ======= Execution =======
calculator = MyCalc()

print(calculator.my_calculator(10, 5, '+'))    # Valid
print(calculator.my_calculator(10, 0, '/'))    # Division by zero
print(calculator.my_calculator("ten", 2, '*'))  # Invalid input
print(calculator.my_calculator(10, 2, '?'))    # Invalid operator

