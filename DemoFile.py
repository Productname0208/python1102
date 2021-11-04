# DemoFile.py

# 파일에 쓰기(write + text mode)
f = open("c:\\work\\demo.txt","wt")
f.write("첫번째\n두번째\n세번째\n")
# 버퍼를 지우고 작업 종료
f.close()

# 파일을 읽기(read + text)
f = open("c:\\work\\demo.txt","rt")
print(f.readline())
print(f.readline())
print("---하나의 문자열로 읽기---")
print(f.tell())
print(f.readlines())
f.seek(0)
# result = f.read()
# print(result)
lst = f.readlines()
print(lst)
f.close()

# 파일 닫았나?
if f.closed:
    print("파일을 닫았습니다.")
else:
    f.close()

# 서식지정문자
print("{0:x}".format(10))   # 16진수
print("{0:b}".format(10))   # 2진수
print("{0:,}".format(15000))    # 3자리마다 ,찍기

