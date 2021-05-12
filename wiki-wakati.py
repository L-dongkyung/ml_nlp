import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec

readFp = codecs.open("wiki.txt", "r", encoding="utf-8")
gubun_file = "wiki.gubun"
writeFp = open(gubun_file, "w", encoding="utf-8")

okt = Okt()
i = 0
while True:
    line = readFp.readline()
    if not line:break
    if i % 20000 == 0:
        print("current - "+str(i))
    i += 1

    malist = okt.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            writeFp.write(word[0] + " ")
writeFp.close()
