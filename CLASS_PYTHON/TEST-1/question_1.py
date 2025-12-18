# Program that takes two numbers as input and prints their sum

num1 = input("ENTER THE FIRST NUMBER: ")
num2 = input("ENTER THE SECOND NUMBER: ")


    
# if "." not in num1 and "." not in num2:
#         var1 = int(num1)
#         var2 = int(num2)
# else:
#         var1 = float(num1)
#         var2 = float(num2)

# sum = var1 + var2
# print(f"SUM: {sum}")


try:
            
    if "." not in num1 and "." not in num2:
        var1 = int(num1)
        var2 = int(num2)
    else:
        var1 = float(num1)
        var2 = float(num2)

    sum = var1 + var2
    print(f"SUM: {sum}")
except:
      print("ITS STRING, ENTER INTEGER OR FLOAT VALUE")    


# fruit = [1,2,3]

# print(1 in fruit)