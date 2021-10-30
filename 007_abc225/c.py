N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

if N == M == 1:
    print('Yes')
    exit()

if M > 1:
    if M == 7 and B[0][6] % 7 != 0:
        print('No')
        exit()
    elif M < 7:
        for i in range(M-1):
            if B[0][i] % 7 == 0:
                print('No')
                exit()

    for i in range(M-1):
        if B[0][i] + 1 != B[0][i+1]:
            print('No')
            exit()

if N > 1:
    for i in range(N-1):
        for j in range(M):
            B[i][j] += 7
        if B[i] != B[i+1]:
            print('No')
            exit()

print('Yes')
