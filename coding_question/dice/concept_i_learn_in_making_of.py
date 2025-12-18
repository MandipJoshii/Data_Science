"""we can import random function and can use randint() function to take random interger specific values from our range we want 

syntax randint(start,stop)

OTHER CONCEPTS:

randrange(start,stop,step)

random() -> can generate random float values 

uniform -> returns a random float number

major difference between random and uniform is:
random can only give in range between 0-1 and uniform can give float value upto how much user has set start and end point
random() function dont take argument and uniform takes argument



other untouch concept/need to read in future

choice(sequence, k=n) -> Returns one random element from a list, tuple, or string.

sample(sequence, k=n) -> Returns k unique random elements (no repetition).

suffle(variable_name) -> suffle list in place 

seed(n) -> Sets the seed for reproducible randomness.

getrandbits(n) -> Returns an integer with n random bits.


"""



import random as rand

dice_roll = rand.randrange(1,7,2) # cant take value in minus

print(dice_roll)

num = rand.random()
print(num)

uni = rand.uniform(1,10)

print(uni)