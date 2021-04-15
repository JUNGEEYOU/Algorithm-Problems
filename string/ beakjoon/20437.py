import sys
from collections import defaultdict
"""
1. 문자열 별로 위치 저장 
2. k개를 포함하는 문자열 중 가장 짧은, 가장 긴 길이 구하기 
"""

def get_word_index(word):
    """
    단어 별 위치 저장
    :return:
    """
    dict_ = defaultdict(list)
    for i, w in enumerate(word):
        dict_[w].append(i)
    return dict_

def get_result(word, k):
    """
    가장 짧은 가장 긴 길이 구하기
    :return:
    """
    dict_ = get_word_index(word)
    min_ = int(1e10)
    max_ = -1
    for key, val in dict_.items():
        if len(val) < k:
            continue
        for i in range(0, len(val) - k + 1):
            res = val[i + k - 1] - val[i] + 1
            if min_ > res:
                min_ = res
            if max_ < res:
                max_ = res
    return (min_, max_)




for _ in range(int(sys.stdin.readline())):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())
    min_, max_ = get_result(w, k)
    if max_ == -1:
        print(-1)
    else:
        print(min_, max_)
