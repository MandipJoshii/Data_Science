# Build a simple grade calculator for multiple students. Input their marks in a list and print the grade using a function.

def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "Fail"
    

mark_grade = [10,20,30,40,50,60,70,80]

# for grade in mark_grade:
#     mark = calculate_grade(grade)

# print(grade)


for grade in mark_grade:
    mark = calculate_grade(grade)
    print(mark)

