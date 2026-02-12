marks = [84,95,76,54,96,88,91,92,95,75,91,97,80]
print("Mean =",sum(marks)/len(marks))
print("Median =",marks[len(marks)//2])
print("Mode =", max(marks, key = marks.count))