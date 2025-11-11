# Program 1: Class and Object Example
# --------------------------------------
# This program demonstrates how to define a class and
# access its attributes and methods using an object.

class Student:
    def __init__(self, name, course):
        self.name = name        # Attribute
        self.course = course    # Attribute

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Enrolled Course: {self.course}")


# Creating an object of the class
student1 = Student("Christian Jason Ranison", "Computer Engineering")

# Accessing properties and methods using the object
student1.display_info()
