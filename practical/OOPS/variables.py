# 🐍 Program 2: Local and Global Variables
# ---------------------------------------
# This program demonstrates the difference between
# local and global variables inside a class.

# Global variable
college_name = "LJIET College"


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name  # Instance variable (attribute)

    def show_info(self):
        # Local variable
        head = "Prof. Mehta"
        print(f"Department: {self.dept_name}")
        print(f"Head of Department: {head}")
        print(f"College: {college_name}")  # Accessing global variable


# Creating object and calling method
dept_obj = Department("Computer Science")
dept_obj.show_info()
