# DemoLoop2.py

# 리스트 컴프리헨션(list comprehensions)
lst = [1,2,3,4,5,6,7,8,9,10]
result = [i**2 for i in lst if i>5]
print(result)

d = {100:"apple", 200:'kiwi'}
print([v.upper() for v in d.values()])

def times(a,b):
    return a*b

print(times(10,10))
print(globals())