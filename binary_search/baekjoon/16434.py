import sys

def binary(target, atk):
    """
    :param target: 예상 최대 생명력
    :param atk:  용사의 공격력
    :return:  True 성공 False 용사가 죽음
    """
    max_target = target
    for t, a, h in arr:
        if t == 1:    # 몬스터
            my_total = h // atk if h % atk == 0 else (h // atk) + 1  # 용사 총 공격 횟수
            # 내 힘에서 내가 공격할 횟수만큼 몬스터가 공격
            target -= (my_total - 1) * a
            if target <= 0:
                return False
        else:         # 포션
            atk += a
            target += h
            if target > max_target:   # 최대 생명력이 초과하는 경우는 최대값으로만 세팅
                target = max_target
    return True


n, atk = map(int, sys.stdin.readline().split())  # 방 수, 용사의 공격력
arr = list()
right = 1
for _ in range(n):
    t, a, h = map(int, sys.stdin.readline().split())
    right += a * h
    arr.append((t, a, h))

left = 1
result = 0
while left <= right:
    mid = (left + right) // 2
    if binary(mid, atk):
        result = mid
        right = mid - 1
    else:
        left = mid + 1
print(result)