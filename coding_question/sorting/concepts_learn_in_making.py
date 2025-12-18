#list() -> ?

"""list splits a integer or string into separate number by number or character by character not word by word"""
var_int = list([1,2,3,4,5,6,7])
var_char = list("abcdefghijk")
var_mix = list([2.4,4,55.9,0.9]) # you cant put string inside numerical value
"""note

doing this ->  var_char = list("abcdefghijk")
will give output -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'f']

but doing this -> var_char = list(["abcdefghijk"])
will give output -> ['abcdefghijk']

its because in first list() function iterated the whole string but when something is inside tuple it is an element/item 
so its index is 0 so index 0 interation will give index 0 value not index 0 iterated value

"""

print(var_int)
print(var_char)
print(var_mix)


#len() = ?

"""
len() function provides total length(in number) of items/elements 

"""

for i in range(len(var_mix)):
    print("i = ", i)

    