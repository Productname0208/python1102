# ifelse.py

print("---ctrl-c를 클릭하면 종료---")

while True: # While 이용해서 keyboard interrupt 전까지 계속 뺑뺑이 돌릴수있음
    score = int(input("점수를 입력: "))

    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score:
        grade = "B"
        grace = "ab"
    else:
        grade = "C"


    print("Grade is " + grade)
