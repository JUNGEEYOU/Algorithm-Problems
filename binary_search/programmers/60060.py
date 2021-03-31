"""
https://programmers.co.kr/learn/courses/30/lessons/64062
"""
import bisect


def get_count(a, left, right):
    return bisect.bisect_right(a, right) - bisect.bisect_left(a, left)



def solution(words, queries):
    answer = []
    wrd = [[] for _ in range(100000)]
    wrd_reverse = [[] for _ in range(100000)]

    for w in words:
        wrd[len(w)].append(w)
        wrd_reverse[len(w)].append(w[::-1])

    for i in range(100000):
        wrd[i].sort()
        wrd_reverse[i].sort()

    for querie in queries:
        if querie[0] == "?":  #
            left = querie[::-1].replace("?", "a")
            right = querie[::-1].replace("?", "z")
            answer.append(get_count(wrd_reverse[len(querie)], left, right))
        else:  # 접미사
            left = querie.replace("?", "a")
            right = querie.replace("?", "z")
            answer.append(get_count(wrd[len(querie)], left, right))
    return answer


print(solution(words=["frodo", "front", "frost", "frozen", "frame", "kakao"], queries=["fro??", "????o", "fr???", "fro???", "pro?"]))