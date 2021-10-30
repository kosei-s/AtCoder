N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def judge(mid: int) -> bool:
    pre, cnt = 0, 0
    for i in range(N):
        if A[i] - pre >= mid:
            cnt += 1
            pre = A[i]
            if cnt == K:
                break
    if cnt == K and L - pre >= mid:
        return True
    else:
        return False

left = -1
right = L + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if judge(mid):
        left = mid
    else:
        right = mid

print(left)
