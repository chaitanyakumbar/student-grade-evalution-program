s1=float(input("enter marks:"))
s2=float(input("enter marks:"))
s3=float(input("enter marks:"))
s4=float(input("enter marks:"))

marks=(s1+s2+s3+s4)/4

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
print("average marks:",marks)
print("student grade:",grade)