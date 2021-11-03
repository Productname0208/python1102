# Class1.py

# 1) 클래스 형식을 정의
class Person:
    # 초기화메서드(생성자)
    def __init__(self):
        self.name = "default name"
    # 인스턴스 메서드
    def print(self):
        print("이름은 ", self.name)

# 2) 인스턴스 생성. 클래스명() 하면 init을 부르도록 되어있음.
p1 = Person()
p2 = Person()

# 3) 인스턴스 메서드 호출
p1.name = "전우치"
p1.print()
p2.print()
