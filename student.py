marks=float(input("enter your marks:"))
if marks >= 90:
    grade ="A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "fail"
print("your grade is:",grade)