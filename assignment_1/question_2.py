#2. Print a multiplication table for a number, but highlight multiples of 5.

#1*5 = 5
num = 6
for i in range(1,11):
    multi = i * num
    if multi % 5 == 0:
        print(f"{i}*{num} = *{multi}")
    else:
        print(f"{i}*{num} = {multi}")    
