N, W = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

current_W = W
delicious = 0
AB = sorted(AB, key=lambda x: x[0], reverse=True)
for ab in AB:
    a = ab[0]
    b = ab[1]
    if current_W >= b:
        current_W -= b
        delicious += a * b
    else:
        delicious += a * current_W
        current_W = 0
    
    if current_W <= 0:
        break

print(delicious)
