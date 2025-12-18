#Read a CSV file of students (name, grade, age) and print only the names.

import pandas as pd

student_detail = pd.read_csv("student_dataset.csv")

for sd in student_detail["Student_Name"]:
    print(sd)
