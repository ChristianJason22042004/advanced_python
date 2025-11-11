# 🐍 Program: Custom Exception Handling in Python
# ------------------------------------------------
# This program demonstrates how to create and use custom exceptions
# to handle specific error conditions gracefully.

# Step 1: Define a custom exception class
class InvalidAgeError(Exception):
    """Raised when the entered age is not within the valid range."""
    pass


# Step 2: Define a function that uses the custom exception
def validate_age(age):
    """Checks if the age is valid (between 0 and 120)."""
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    elif age > 120:
        raise InvalidAgeError("Age seems unrealistically high.")
    else:
        print("✅ Age is valid!")


# Step 3: Use try-except to handle the custom exception
try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)

except InvalidAgeError as e:
    print(f"❌ Custom Exception: {e}")

except ValueError:
    print("⚠️ Please enter a valid integer value for age.")

finally:
    print("🎯 Program execution completed.")
