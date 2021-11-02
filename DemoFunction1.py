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