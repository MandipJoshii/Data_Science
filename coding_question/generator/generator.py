#Create a generator that yields numbers from 1 to 5 one by one. (generators)


def generate_number():
    for i in range(1,6):
        yield i
        # yield i
        print("hello")

num = generate_number()

for n in num:
    print(n)

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 1
#     yield 2
#     yield 3


# g = gen()

# for i in g:
#     print(i)

# def gen():
#     return 1
#     # return 2


# gen = gen()
# print(gen)
# for g in gen:
#     print(g)