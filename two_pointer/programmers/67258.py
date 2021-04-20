from collections import defaultdict


def solution(gems):
    len_gem = len(set(gems))
    left = 0
    right = 0
    kinds = defaultdict(int)
    kinds[gems[0]] += 1
    min_ = (len(gems) - 1, 1, len(gems))
    while right < len(gems):
        # 모든 종류를 가진 경우
        if len(kinds) == len_gem:
            if min_[0] > right - left:
                min_ = (right - left, left + 1, right + 1)
            kinds[gems[left]] -= 1
            if kinds[gems[left]] == 0:
                del kinds[gems[left]]
            left += 1
        else:
            # 모든 종류를 가지지 않은 경우, right +1
            if right < len(gems) - 1:
                right += 1
                kinds[gems[right]] += 1
            else:
                break


    return list(min_[1:3])

print(solution(gems=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))