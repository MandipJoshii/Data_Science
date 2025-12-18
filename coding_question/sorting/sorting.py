#You are given marks of students. Sort them from highest to lowest. (sorting)
#core logic = compare then swap using temp with a and b
import pandas as pd

marks = pd.read_csv("student-mat.csv", delimiter=";")
print(marks.head())
print(marks["G3"][2] > marks["G3"][0])

marks_list = list(marks["G3"])

marks_list.sort() #in default lower to high if used reverse=True then sorts from high at first and lowest at last
print(marks_list)
# # print(marks_list)
for i in range(len(marks_list)):
    for j in range(i+1, len(marks_list)):
        if marks_list[i] < marks_list[j]:
            temp = marks_list[i]
            marks_list[i] = marks_list[j]
            marks_list[j] = temp

""""or we can also do:
marks_list[i], marks_list[j] = marks_list[j],marks_list[i]

where what we are doing is python is storing the marks_list of i and j in temp1 and temp2 from right hand side

its like doing:
temp1 = marks_list[j]
temp2 = marks_list[i]

and then in mark_list[i] the temp1 value goes which is of marks_list[j] and for marks_list[j] the temp2 value goes
"""            

print("sorted: ", marks_list)            

    