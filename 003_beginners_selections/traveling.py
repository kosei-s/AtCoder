n = int(input())

cnt, now_t, posx, posy = 0, 0, 0, 0
flg = True
while cnt < n and flg:
    t, x, y = map(int, input().split())

    if abs(posx - x) + abs(posy - y) > t - now_t:
        print('No')
        flg = False
    elif (t - now_t) % 2 == 0 and (abs(posx - x) + abs(posy - y)) % 2 != 0:
        print("No")
        flg = False
    elif (t - now_t) % 2 != 0 and (abs(posx - x) + abs(posy - y)) % 2 == 0:
        print('No')
        flg = False
    else:
        cnt += 1
        now_t = t
        posx = x
        posy = y
if flg:
    print('Yes')
