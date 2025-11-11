# Write a Python program to open a file in write mode, write some text,
# and then close it

# write mode will either overwrite existing files if file exist or
# creates a new file
my_file = open("jason.txt", "w")
my_file.write("About Jason Ranison Christian")
# we have to close a file also , it is mandatory and file must be closed
# if created.
my_file.close()

# Practical Example:
# 3) Write a Python program to create a file and write a
# string into it.

my_file_create = open("about_jason.txt", "w")
lines = ["Jason knows Python\nAlongside with HTML,CSS and JS."]
my_file_create.writelines(lines)
my_file_create.close()
