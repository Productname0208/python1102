# Class1.py

# 1) 클래스 형식을 정의
class Person:
    # 위치를 잘 본다~~
    num_person = 0
    # 초기화메서드(생성자)
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
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

# 인스턴스 갯수 확인
print("몇 개: ",Person.num_person)

p2.num_person = 5
print(p2.num_person)
print(p1.num_person)
print(Person.num_person)

# 런타임(코드가 실행중) 시에 변수를 추가(동적인 형식의 언어)
# 디자인타임(개발하고 있는 시점)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)/

p1.age = 30
print(p1.age)
# print(p2.age)