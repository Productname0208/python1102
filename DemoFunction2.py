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
