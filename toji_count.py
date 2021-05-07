import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt

# utf-16 encoding
fp = codecs.open("bexx0003.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body > text")
text = body.getText()

### 국립 국어원 언어정보나눔터에서 토지 다운로드 ###

# text one line process
okt = Okt()
word_dic = {}
lines = text.split("\n")  # 문서를 줄 단위로 분할
for line in lines:
    malist = okt.pos(line, stem=True)  # 줄별 단어에 명사, 동사 등 명시 -- stem 은 형대소를 원형으로
    for word in malist:  # 줄단위로 포문을 돌림
        # if word[1] == "Noun": # 명사 확인 -- 품사 별 선별
        if word[1] == "Verb": # 동사 확인
            if not (word[0] in word_dic):  # 워드사전에 단어가 있는지 확인
                word_dic[word[0]] = 0  # 워드사전에 단어가 없으면 0으로 초기화
            word_dic[word[0]] += 1 # 카운트하기  # 단어에 갯수 추가

# 많이 사용된 명사 출력
keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()