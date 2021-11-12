# web1.py
from bs4 import BeautifulSoup

# 페이지를 로딩
page = open("c:\\work\\test01.html","rt",encoding="utf-8").read()   # rt:read&text. encoding="utf-8": 유니코드를 지칭. read(): 하나의 문자열로 읽음
# 검색이 용이한 객체
# 정해져있는 상수같은 느낌의 코드임
soup = BeautifulSoup(page,"html.parser")    # BeautifulSoup: class. html.parser: html을 읽어서 처리하겠다.
print(soup.prettify)

# <p> p태그 몽땅 검색
print(soup.find_all("p",class_="outer-text"))   # find는 하나만 가져옴

# 태그는 삭제하고 컨텐츠만 가져오기
for tag in soup.find_all("p"):
    content = tag.text
    print(content.strip())
