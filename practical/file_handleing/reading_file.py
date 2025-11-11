# Write a Python program to read the contents of a file and print them on the console.

with open("about_jason.txt", "r") as f:
    read = f.read()

print(f"content of the file in console is here : {read}")
# Write a Python program to write multiple strings into a file.


with open("jason.txt", "w") as w_pointer:
    w_pointer.writelines(
        ["he has various hoobies too like,\nsinging and \nreading lores"])

print("overwritten in exisitng file")
print("😁 Sucess")

# Demonstrate tell() to check file pointer position
with open("about_jason.txt", "r") as f1:
    print("Initial Cursor Position:", f1.tell())   # At start (0)

    data = f1.readline()  # Read first line
    print(f"After reading one line, {repr(data)}")
    print(f"initial cursor position is {f1.tell()}")

    data2 = f1.read(10)  # Read next 10 characters
    print(f"After reading 10 more characters, string is {repr(data2)}")
    print(f"cursor position after reading 10 characters is {f1.tell()}")
