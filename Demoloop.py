# Demoloop.py

# 계산을 해야하는 경우
value = 5
abc = 0
while value > 0:
    print(value)
    value -= 1
    abc += 1

print("계산횟수:", abc)

# 갯수를 이미 알고 있는 경우
lst = ["apple", 100, 3.14]  # list. 순서 있고 읽기,쓰기,삭제,수정 다 가능
print("갯수:",len(lst))
for item in lst:
    print(item, type(item))

# 딕셔너리
d = {"apple":100, "kiwi":200, "orange":300}

for item in d.items():
    print(item)

