# DemoFunction2.py

# 기본값이 있는 경우
def times(a=10, b=20):
    return a*b

# 호출
print(times())
print(times(5))
print(times(b=6))
print(times(a=3,b=4))

# 키워드 인자방식
def connectURI(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

# 호출
print(connectURI("credu.com","80"))
print(connectURI(port="80",server="credu.com"))

# 가변인자(갯수가 정해지지 않은 경우)
def union(*ar): # *누르면 갯수 모를 때 가능. *는 tuple변수 받음
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))

# 정의되지 않은 인자: 필수와 옵션이 있는 경우
def userURIBuilder(server,port,**user): # 앞에 있는 변수는 필수. 뒤에 있는 변수를 옵션으로 해야함.
    str = "https://" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

print(userURIBuilder("test.com","8080",id="kim",passwd="1234"))
print(userURIBuilder("credu.com","80",id="kim",passwd="1234",name="mike",
age="30"))
# 괄호 안닫았으면 엔터쳐도 한 줄의 코드로 인식
# 다른 것에서 한줄로 인식하려면 \ 백슬래시 입력하면 됨.

# 람다함수: 이름이 없는 함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))
print(globals())