import numpy as np

marks = np.array([
    45, 67, 89, 90, 56, 78, 88, 92, 34, 60,
    71, 84, 76, 59, 63, 85, 91, 72, 68, 74,
    80, 82, 77, 69, 65, 70, 73, 79, 83, 86,
    87, 75, 66, 62, 58, 55, 52, 49, 47, 44,
    90, 88, 85, 78, 74, 71, 69, 67, 65, 63
])

# print(marks)
# marks_mean = marks.mean()
marks_mean = np.mean(marks)

print("Means: ",marks_mean)

marks_median = np.median(marks)

print("Median: ",marks_median)

values, counts = np.unique(marks, return_counts=True)
mode_marks = values[np.argmax(counts)]

print("Mode:", mode_marks)

Q1 = np.percentile(marks, 25)
Q3 = np.percentile(marks, 75)

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("Interquartile Range (IQR):", IQR)

