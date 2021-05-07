from konlpy.tag import Okt
okt = Okt()
malist = okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
print(malist)
# 5가지 형태소 분석기가 있지만 Kkma 와 Oky 사용. 이중 Okt 가 품사를 잘 읽어 이것 사용.

