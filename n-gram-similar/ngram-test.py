def ngram(text, num):
    res = []
    slen = len(text) - num +1
    for i in range(slen):
        ss = text[i:i+num]
        res.append(ss)
    return res

def diff_ngram(texta, textb, num):
    a = ngram(texta, num)
    b = ngram(textb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b :
            if i == j:
                cnt +=1
                r.append(i)
    return cnt / len(a), r


text1 = "오늘 강남에서 맛있는 스파게티를 먹었다."
text2 = "강남에서 먹었던 오늘의 스파게티는 맛있었다."
# 2-gram
r2, word2 = diff_ngram(text1, text2, 2)
print("2-gram:", r2, word2)

# 3-gram
r3, word3 = diff_ngram(text1, text2, 3)
print("3-gram:", r3, word3)