def main():
    t = int(input())
    cases = [list(map(int, input().split())) for i in range(t)]

    ans = 0
    for case in cases:
        a, b, c = case
        for i in range(3):
            if i == 0:
                t1 = a
                t2 = b
                t3 = c
            elif i == 1:
                t1 = b
                t2 = c
                t3 = a
            else:
                t1 = c
                t2 = a
                t3 = b

            if abs(t1-t2) % 3 == 0:
                q = abs(t1-t2) // 3
                if t3 >= q:
                    if t1 == t2:
                        ans = t1
                    elif t1 > t2:
                        ans = q + t2
                    else:
                        ans = q + t1
        if ans > 0:
            print(ans)
        else:
            print('-1')



if __name__ == '__main__':
    main()
