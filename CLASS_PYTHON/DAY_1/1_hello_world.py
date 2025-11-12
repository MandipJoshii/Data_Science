import sys 

"""
code block defined by indentaion, not brackes
use 4 spaces not tabs
case_sensitive

data types: variable ma pathako data kun type ko ho
int
float
boolean
string
tist
tuples
sets
dict
null
"""

#string 
name = "mandip"

#integer
age = 22

#float
height = 5.5

#boolean = true/false
check_age = True

#list
number = [1,2,3,4]

#tuple + string
fruits = ("apple","banana")

#set
random = {1,2,3,4,"a","b","c","d"}

#dictionary
user_detail = {
    "name":"mandip",
    "age":21,
    "height":5.5
}

#null
is_null = None

print("\n")
print("HELLO WORLD")
print(name)
print(age)
print(height)
print(check_age)
print(number)
print(fruits)
print(random)
print(user_detail)
print(is_null)

x = 10
y = "20"
# z = int(y)+x
# print(z)
# print(int(y)+x)
z = y + str(x)
print(z)

#assignment
#all the words that cannot be used as variables in python

"""
1. cannot be reserved keywords like if, else, elif, for, while etc
2. cannot have space or special characters in the beginning of the variable like $,%,^ etc
3. cannot have space between the variable
4. cannot have number between the variable
"""



#list all the naming convention rules in python
"""

"""




#list all the possible special characters that cannot be used in variables in python

"""

"""

#data types values, can we reduce the byte(size) of the data types like if string has 4 byte then can we make it upto 2 bytes, how is it done and how is it applied int he code

#python all operators explain in class

num = 123456789
string = "mandip_joshi"

print(sys.getsizeof(num))
print(sys.getsizeof(string))
print("\n")


#arithmetic operator
a = 4
b = 15

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a**b)
print(a//b)

print("\n")

#assignment operator
a+=3
print(a)
# print(a-=3) we cant do like this because its an statement not an expression where statement is a = 2 and expression is print(1+1)
a-=3
print(a)
a*=3
print(a)
a/=3
print(a)
a%=3
print(a)
a**=3
print(a)
a//=3
print(a)

print("\n")


#logical operand
x = 4
y = 15
print(x>3 and y<20) #4>3 and 15<20
print(x>20 or y>5)
print(not(b>2))





#comparison operand
print("\n")
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


#bitwise operator - performs operation on binary number

print("\n")

print(x&y)
print(x|y)
print(x^y)
print(x>>2)
print(x<<2)
print(~x)


print("\n")


#membership operator - checks if x is a part of y value sequent
m = ["avocado","straberry","mango"]
d = 4
i = m
print("mango" in m)
print("mango" not in m)
print("\n")
#identity opertor - compare objects identity not value
print(m is i) #(same memory)
print(m is not i)







