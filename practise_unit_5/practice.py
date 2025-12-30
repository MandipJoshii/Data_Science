#list 

myList = [1,2,3,4,"a","b","c"]

myList.append(1) # add at last

print(myList)

myList.pop()

print(myList)

myList.insert(1,3) #(index,value)

print(myList)

myList.remove(1)

print(myList)


myList.sort(key=str)

print(myList)

myList.reverse()

print(myList)






#tuple


myTuple = (1,2,3,4,5,6,7,8)
word = "Gate Smashers"

print(myTuple[1:5])
print(myTuple[:5])
print(myTuple[5:])

print(word[5:10])



print(myTuple[-7:-3])
print(myTuple[-7:-3:2])

print(myTuple[::-1])

# print(myTuple[12])



A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))
print(A.intersection(B))
print(B.difference(A))
print(A.symmetric_difference(B))