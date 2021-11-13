# 解説見ても何がだめなのかわからない。。
import math


N = int(input())

cnt = 0
for a in range(1, int(math.pow(N, 1/3)) + 1):
    for b in range(a, int(math.sqrt(N / a)) + 1):
        cnt += N // (a * b) - b + 1

print(cnt)
