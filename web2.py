# web2.py
# 웹서버에 요청
import urllib.request
# 웹크롤링
from bs4 import BeautifulSoup

# 패키지명.파일명.함수명
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

# 파일에 저장
f = open("c:\\work\\webtoon.txt","wt",encoding="utf-8") # 한글포함되어서 utf-8 넣어주기

# 수열함수로 페이지 번호를 1~5 생성
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="+str(i) # 페이지번호 1~5 넘겨가며 url 지정
    print(url)
    data = urllib.request.urlopen(url)

    # 검색이 용이한 객체를 생성
    soup = BeautifulSoup(data,"html.parser")

    # <td class="title">
    # 				<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','50')">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
    # 						</td>
    cartoons = soup.find_all("td",class_="title")   # class는 기본어이므로 class_로 입력
    print("갯수:{0}".format(len(cartoons)))
    title = cartoons[0].find("a").text  # find_all하면 10개 목록 있기때문에 그 중에 첫번째 꺼를 뽑아서 text만 뽑아라
    link = cartoons[0].find("a")["href"]
    print(title)
    print(link)

    # 반복해서 가져오기
    for tag in cartoons:
        title = tag.find("a").text  # find_all하면 10개 목록 있기때문에 그 중에 첫번째 꺼를 뽑아서 text만 뽑아라
        print(title.strip())
        f.write(title.strip("마음의 소리")+"\n")

f.close()
        
