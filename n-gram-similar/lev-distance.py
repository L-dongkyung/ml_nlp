# 레벤슈타인 거리 구하기
def calc_distance(base, sample):
    '''레벤슈타인 거리 계산하기 '''
    if base == sample : return 0
    base_len = len(base)
    sample_len = len(sample)
    if base == "": return sample_len
    if sample == "": return base_len
    
    # 2차원 표(a_len + 1, b_len + 1) 준비하기
    matrix = [[] for i in range(base_len+1)]
    for i in range(base_len+1):  # 0으로 초기화
        matrix[i] = [0 for j in range(sample_len+1)]
    
    # 0일때 초기값을 설정
    for i in range(base_len+1):
        matrix[i][0] = i
    for j in range(sample_len+1):
        matrix[j][0]= j
    
    # 표 채우기
    for i in range(1, base_len+1):
        ac = base[i-1]
        for j in range(1, sample_len+1):
            bc = sample[j-1]
            cost = 0 if (ac==bc) else 1
            matrix[i][j] = min([matrix[i-1][j] + 1,  # 문자 삽입
                                matrix[i][j-1] + 1,  # 문자 제거
                                matrix[i-1][j-1] + cost  # 문자 변경
                                ])
    return matrix[base_len][sample_len]


# "가나다라"와 "가마바라"의 거리
print(calc_distance("가나다라", "가마바라"))

# 실행 예
samples = ["신촌역", "신천군", "신천역", "신발", "마곡역", ""]
base = samples[-1]
# r = sorted(samples, key= lambda n: calc_distance(base, n))
for n in samples:
    print(calc_distance(base, n), n)
