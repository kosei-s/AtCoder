N = int(input())
S = list(map(int, input().split()))

cnt = 0
for s in S:
    check = False
    for a in range(1, s // 4 + 1):
        for b in range(1, s // 4 + 1):
            if s == 4 * a * b + 3 * a + 3 * b:
                check = True
                break
        if check:
            break
    if not check:
        cnt += 1
    else:
        check = False

print(cnt)
