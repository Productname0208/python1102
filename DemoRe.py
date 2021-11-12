# DemoRE.py

# 정규표현식
import re   # re모듈(정규표현식 모듈)

# 찾았으면 매칭 객체 리턴
result = re.search("[0-9]*th","35th")
print(result)
print(result.group())

# match함수, search 함수 비교
# match는 정확하게 일치(포함 X)
# search는 포함하고 있다면 True(일반적인 검색)
print(bool(re.match("ap","this is apple")))
print(bool(re.search("ap", "this is apple")))

print("---년도---")
print(bool(re.match("\d{4}","작년은 2020년, 올해는 2021년")))
print(bool(re.search("\d{4}","작년은 2020년, 올해는 2021년")))
print(re.search("\d{4}","작년은 2020년, 올해는 2021년").groups())