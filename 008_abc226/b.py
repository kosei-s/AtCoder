N = int(input())
L = []
a = []
for i in range(N):
    inputs = list(map(int, input().split()))
    L.append(inputs[0])
    a.append(inputs[1:])
a = [tuple(prog) for prog in a]
a = set(a)

print(len(a))
