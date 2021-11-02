# DemoFunction1.py

# 함수를 정의
def setValue(newValue):
    x = newValue

# 함수를 호출
result = setValue(5)
print(result)

# 함수를 정의
def swap(x,y):
    return y,x

# 함수를 호출
print(swap(5,6))

# 디버깅 연습을 위한 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 함수를 호출
print(intersect("HAM","SPAM"))
print(intersect("가","나"))

# 정수, 실수, 복소수, 문자열, 튜플, 불린: 불변형 변수
print("---불변형식---")
x = 1.2
print(id(x))
x = 2.3
print(id(x))

print("---가변형---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst),lst)

abc = lst[:]
efg = lst

print(id(abc), id(efg), id(lst))

# 참조를 통해서 인자를 전달
def change(x):
    # 함수 내부에 복사본을 만들어서 작업(DeepCopy)
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:",x1)

# 함수를 호출
wordlist = ["J","A","M"]
change(wordlist)    # list(가변형)의 참조를 그대로 가져가므로 wordlist가 바뀜
print(wordlist)

# 전역변수와 지역변수
x = 1
def func(a):
    return x+a

# 함수 호출
print(func(1))

def func2(a):
    x = 5
    return x+a

print(func2(1))