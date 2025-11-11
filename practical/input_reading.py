# Program 1: Read name and age, then display formatted output
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nHello {name}, you are {age} years old.")

# Program 2: Read a string, an integer, and a float, then display them
string_value = input("\nEnter a string: ")
integer_value = int(input("Enter an integer: "))
float_value = float(input("Enter a floating-point number: "))

print("\n--- Displaying Entered Values ---")
print(f"String value: {string_value}")
print(f"Integer value: {integer_value}")
print(f"Float value: {float_value:.2f}")  # formatted to 2 decimal places
