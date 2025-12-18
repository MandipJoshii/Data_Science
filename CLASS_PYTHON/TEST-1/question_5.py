# #find even and odd

# num = int(input("ENETR A NUMBER: "))

# if num % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")

num = input("ENTER A NUMBER: ")
try:
    var = int(num) 

    
    if var % 2 == 0:
     print("EVEN") 
    else:
     print("ODD")  
except:
   print("CANT TAKE FLOAT,STRING AND OTHER SPECIAL CHARACTERS")                