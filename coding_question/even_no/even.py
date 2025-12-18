#Create a list of even numbers only from 1 to 20. (list comprehension)
evens = [num for num in range(1,21) if num % 2 == 0]   
print(evens)