import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
import urllib.request

import os, re, json, random

# 딕셔너리에 데이터 등록하기
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

# 마르코프 체인 딕셔너리 마들기
def make_dic(words):
    tmp = ["@"]
    dic ={}
    for word in words:
        tmp.append(word)
        if len(tmp) < 3 : continue
        if len(tmp) > 3 : tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == ".":
            tmp = ["@"]
            continue
    return dic

# 문장 만들기
def make_sentence(dic):
    ret=[]
    if not "@" in dic : return "no dic"
    top = dic["@"]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3= word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == ".": break
        w1, w2 = w2, w3
    ret = "".join(ret)
    '''  # 띄어쓰기 생략
    # 띄어쓰기
    params = urllib.parse.urlencode({"_callback": "", "q": ret})
    # 네이버 맞춤법 검사기를 사용
    # data = urllib.request.urlopen("http://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy?" + params)
    data = urllib.request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%A7%9E%EC%B6%A4%EB%B2%95+%EA%B2%80%EC%82%AC%EA%B8%B0" + params)
    data = data.read().decode("utf-8")[1:-2]
    data = json.loads(data)
    data = data["message"]["result"]["html"]
    data  = BeautifulSoup(data, "html.parser").getText()
    '''
    return ret  # data

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

# 문장 읽어 들이기
toji_file = "toji.txt"
dict_file = "markov-toji.json"
if not os.path.exists(dict_file):
    # 토지 텍스트 파일 읽어 들이기
    fp = codecs.open("BEXX0003.txt", "r", encoding="utf-16")
    soup = BeautifulSoup(fp, "html.parser")
    body = soup.select_one("body > text")
    text = body.getText()
    text = text.replace("...", "")
    # 형태소 분석
    okt = Okt()
    malist = okt.pos(text, norm=True)
    words = []
    for word in malist:
        # 구두점 등은 대상에서 제외(단 마침표는 포함)
        if not word[1] in ["Punctuation"]:
            words.append(word[0])
        if word[0] == ".":
            words.append(word[0])
    # 딕셔너리 생성
    dic = make_dic(words)
    json.dump(dic, open(dict_file, "w", encoding="utf-8"))
else:
    dic = json.load(open(dict_file,"r"))

# 문장 만들기
for i in range(3):
    s = make_sentence(dic)
    print(s)
    print("------")


'''
실행 결과:
자넨몸이아파서
낯짝보아하니간밤에잠이깨어옷매무새를고치며으름장을놓다가땅바닥에흩어진곡식알을낳기도전에계영한일이네만하기는그만갔이믄그라십니까뒤통수에들으며용이는망태를본다.
------
노젓는소리로울었다.
------
자꾸자꾸올라가믄수미산이있다캅디다.
------
'''