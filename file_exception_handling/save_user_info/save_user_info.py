#Take a user's name and age and save it to a text file using write or append mode.

name = input("ENTER YOUR NAME: ")
age = int(input("ENTER YOUR AGE: "))

with open("user_info.txt", "a") as f:
    f.write(f"\nYour name is: {name}\n")
    f.write(f"Your age is {age}\n")
    f.write("new entry")

