N = int(input())

S = {}
for _ in range(N):
    s = input()
    try:
        S[s] += 1
    except KeyError:
        S[s] = 1

max = 0
ans = ''
for s, cnt in S.items():
    if cnt > max:
        max = cnt
        ans = s

print(ans)
