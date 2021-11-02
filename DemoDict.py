# DemoDict.py

device = {"아이폰":5, "아이패드":10,"윈도우":20}

print(type(device))

# 입력
device["맥북"] = 15

# 검색
print(device["아이폰"])

# 수정
device["아이폰"] = 6

# 삭제
del device["아이패드"] # 키를 입력해야함
print(device)

# 참조를 복사
device2 = device
print(device2)
device2["LG그램"] = 40
print(device2)
print(id(device),id(device2))
print(device)