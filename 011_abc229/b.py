A, B = tuple(input().split())

figures_cnt = 0
if len(A) > len(B):
    figures_cnt = len(B)
else:
    figures_cnt = len(A)

ans = 'Easy'
for i in range(figures_cnt):
    index = (i + 1) * (-1)
    if int(A[index]) + int(B[index]) >= 10:
        ans = 'Hard'
        break

print(ans)
