# ifelse.py

score = int(input("점수를 입력: "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score:
    grade = "B"
else:
    grade = "C"

print("Grade is "+grade)
