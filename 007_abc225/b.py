N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

if edges[0][0] in edges[1]:
    root = edges[0][0]
elif edges[0][1] in edges[1]:
    root = edges[0][1]
else:
    print('No')
    exit()

for i in range(2, N-1):
    if root not in edges[i]:
        print('No')
        exit()
print('Yes')
