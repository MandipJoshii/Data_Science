# Write a program that prints all prime numbers up to a given number ‘n’.

num = int(input("NUM: "))

for i in range(2, num + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:   
            is_prime = False
            break
    if is_prime:
        print(i, "PRIME")
    else:
        print(i, "COMPOSITE")