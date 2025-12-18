#Write a program that checks if a given string is palindrome.

#cheatcode left side -> positive number, negative number -> (theyo matra jhickne suru dekhi nai) -> for ::num
#cheatcode right side -> positive number, negative number -> (theyo matra jhickne bich dekhi nai) -> for num::
in_Str = input("ENTER A STRING: ")

if in_Str == in_Str[::-1]:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")    

print(in_Str[::-2])
print(in_Str[::2])

print(in_Str[2::])
print(in_Str[-2::])


