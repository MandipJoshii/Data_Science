# count_line = 0
# count_word = 0

# with open("user_info.txt","r") as f:
#     for count in f:
#         count_line += 1
#         count_word += len(count.split())
# print(count_line)      
# print(count_word)  


# with open("user_info.txt", "r") as f:
#     print("read: ", f.read(), "\n")

#     f.seek(0)

#     print("readline: ", f.readline(), "\n")

#     f.seek(0)

#     print("readlines: ",f.readlines(), "\n")

#     f.seek(0)

# Empty dictionary
# data = {}

# while True:
#     key = input("Enter field name (name/age/marks/etc): ")
#     value = input("Enter value: ")

#     data[key] = value  
#     choice = input("Do you want to add more? (yes/no): ")

#     if choice == "no":
#         break

# print("Final Dictionary:")
# print(data)



students = []

while True:
    print("\n1. Add Student  2. List Students  3. Search Student  4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("enter name: ")
        age = int(input("enter age: "))
        grade = int(input("enter grade: "))
        student = {
            "name":name,
            "age":age,
            "grade":grade
        }
        students.append(student)

    elif choice == "3":
        for s in students:
            print(s)   

    elif choice == 4:
        search_name = input("ENTER THE NAME YOU WANT TO SEARCH: ")
        for s in students:
            if s["name"] == search_name:
                print(f"name:{s['name']}, age:{s['age']}, grade:{s['grade']} \n")


    elif choice == "4":
        break 
      