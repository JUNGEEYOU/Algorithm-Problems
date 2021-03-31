def cnt(target, stones, k):
    now = -1
    next = 0
    while next != len(stones):
        if stones[next] >= target:   # 해당 인원인 모두 건너면
            now = next
            next += 1
        else:   # 해당 인원이 못 건너면
            next += 1
            if next - now > k:
                return False
    return True

def solution(stones, k):
    answer = 0
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        if cnt(mid, stones, k):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(solution(stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], k=3 ))