# DemoDict2.py

tel = {"kim":"1111", "lee":"2222"}

phone = tel

print(tel)
print(phone)
print(tel)

# 불린(bool)
isRight = True
print(type(isRight))
x = 5
y = 5

print(x == y)
print(x != y)
print(2>1)
print(5/2)
print(5//2) # 나눗셈 몫
print(5%2) # 나눗셈 나머지

# and는 ~이고, ~이면서
# or연산자는 ~이거나
print(True and True and True)   # 모두 True여야 True
print(True and True and False)
print(True or False or False)   # 하나라도 True면 True

# 파이썬의 판단 근거
print(bool(0))
print(bool(1))
print(bool(""))
print(bool([1,2,3,]))

# 얕은 복사
a = [1,2,3]
b = a
a[0]  = 38
print(a,b)
print(id(a),id(b))

# 얕은 복사
a = [1,2,3]
b = a[:]
a[0]  = 38
print(a,b)
print(id(a),id(b))