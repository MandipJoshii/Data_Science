# Roll a dice 10 times using random.randint() and count how many times you get 6.


import random 
count = 0

for i in range(1,10):
    dice = random.randint(1,6)
    if dice == 6:
        count += 1

print("number of times 6 cames in dice: ", count)

    
