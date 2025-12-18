# Write a program to open a text file and print all its contents. Handle FileNotFoundError.


try:
    with open("file.txt", "w") as f:
        f.write("hello \n")
        f.write("learning")


    with open('file.txt', "r") as f:
        print(f.read())


except FileNotFoundError:
    print("please create the file properly")
   
    