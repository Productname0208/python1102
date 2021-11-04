# DemoStr.py

# 멤버 목록
# print(dir(str))

strA = "python is very powerful"
print(len(strA))
print(strA.capitalize())
print(strA.count("p"))
print(strA.endswith("ful"))

names = ["전우치","이순신","김유신"]
for name in names:
    print("안녕하세요 멋진 가을입니다. {0}님".format(name))
    print("="*40)

# 문자열 가공
u = "<<<   spam and ham   >>>"
print(u)
result = u.strip("<> ") # 양끝에있는 <, >, 공백 제거
print(result)
result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print("---하나의 문자열로 합치기---")
print(":)".join(lst))   # join: 리스트의 각 요소 사이에 :) 집어넣어 하나의 문자열로 합침
