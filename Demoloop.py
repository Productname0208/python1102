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

for k in d.keys():
    print(k)

# 구구단
for i in [2,3,4,5,6]:
    print("---%d단---" % i)
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i,j,i*j))

# 삼각형 출력
for i in range(1,11):
    print("*"*i)


lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
    # 다중라인 주석처리 ctrl+/
    if i > 5:
        break
    print("item:{0}".format(i))

print("---continue---")
for i in lst:
    if i % 2 == 0:
        continue
    print("item:%d" % i)

# 수열함수
result = list(range(2000,2022))
print(result)
day = list(range(1,32))
print(day)

# for ~ in ==> for 루프
for i in range(1,10):
    print(i)