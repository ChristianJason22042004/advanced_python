# ==============================================================
# 🐍 Program: Method Overloading & Method Overriding in Python
# --------------------------------------------------------------
# Author : Christian Jason Ranison
# Purpose: Demonstrate Method Overloading & Method Overriding
# Module : Python OOP Concepts (Assessment Grade Code)
# ==============================================================


# ==============================================================
# 🔹 METHOD OVERLOADING
# --------------------------------------------------------------
# Definition:
# Python does not support true method overloading like Java or C++.
# Instead, it allows simulating overloading by using:
#  - Default parameters
#  - *args or **kwargs (variable-length arguments)
# ==============================================================

class Calculator:
    """A class to demonstrate simulated method overloading in Python."""

    def add(self, a=0, b=0, c=0):
        """
        Adds up to three numbers and returns the sum.
        Uses default arguments to allow flexible input.
        """
        return a + b + c


# ==============================================================
# 🔹 METHOD OVERRIDING
# --------------------------------------------------------------
# Definition:
# Method overriding allows a child class to redefine a method
# from its parent class, enabling runtime polymorphism.
# The child class can also call the parent method using super().
# ==============================================================

class Animal:
    """Parent class defining a generic sound behavior."""

    def sound(self):
        """Displays a general sound message for animals."""
        print("🐾 Some generic animal sound...")


class Dog(Animal):
    """Child class overriding the parent class method."""

    def sound(self):
        """Displays a specific sound for dogs and calls parent method."""
        super().sound()  # Calling the parent method using super()
        print("🐶 Dog barks: Woof! Woof!")


# ==============================================================
# 🔹 MAIN EXECUTION
# ==============================================================

def main():
    """Main function to execute both examples."""
    print("=" * 60)
    print("⚙️  METHOD OVERLOADING & METHOD OVERRIDING DEMONSTRATION")
    print("=" * 60)

    # Method Overloading Example
    print("\n📘 Demonstration 1: Method Overloading (Simulated)")
    calc = Calculator()
    print(f"Sum of one number (5): {calc.add(5)}")
    print(f"Sum of two numbers (5, 10): {calc.add(5, 10)}")
    print(f"Sum of three numbers (5, 10, 15): {calc.add(5, 10, 15)}")

    # Method Overriding Example
    print("\n📗 Demonstration 2: Method Overriding with super()")
    dog = Dog()
    dog.sound()

    print("\n🎯 Program Execution Completed Successfully!")
    print("=" * 60)


# ==============================================================
# 🔹 ENTRY POINT
# ==============================================================

if __name__ == "__main__":
    main()
