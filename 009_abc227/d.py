# 計算量的にだめ。これ数学の問題やん。。
N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == K:
    print(min(A))
    exit()

cnt = 0
A.sort(reverse=True)
while A[K-1] > 0:
    # print(A)  # d
    diff = A[K-1] - A[K]
    if diff == 0:
        diff = 1
    A[0:K] = list(map(lambda x: x - diff, A[0:K]))
    cnt += diff
    A.sort(reverse=True)
# print(A)  # d
print(cnt)
