#Write a program that asks for three numbers and prints the largest using a
#function.

num1 = int(input("ENTER A FIRST NUMBER: "))
num2 = int(input("ENTER A SECOND NUMBER: "))
num3 = int(input("ENTER A THIRD NUMBER: "))


if num1 > num2 and num1 > num3:
    print("num1")
elif num2 > num1 and num2 > num3:
    print("num2")  
else:
    print("num3")      




