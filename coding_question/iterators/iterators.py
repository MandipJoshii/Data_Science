#Convert a list into an iterator and print elements using next(). (iterators)
#a next can be only be used on a iterable thing using iter() functionin
num = [1,2,3,4,5,6,7,8,9]
loop = iter(num)


print(next(loop[4]))
print(next(loop))
print(next(loop))
print(next(loop))
print(next(loop))
print(next(loop))
print(next(loop))
print(next(loop))
print(next(loop))
print(next(loop))#stop iteration error -> we try to get to the next item on iteration process but there is no item found in the iteration process
