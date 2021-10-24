def main():
    n, m = map(int, input().split())
    p = []
    for i in range(n):
        p.append(i+1)
    ab_list = []
    for i in range(m):
        ab = list(map(int, input().split()))
        if ab[0] > n or ab[1] > n:
            print(-1)
            return
        ab_list.append(ab)

    # print(p)  # debug
    for i in range(m // 2):
        for ab in ab_list:
            a = ab[0]
            b = ab[1]
            # print(f'a={a}, b={b}')  # debug
            a_index = p.index(a)
            b_index = p.index(b)
            # print(f'a_index={a_index}, b_index={b_index}')  # debug
            if a_index > b_index:
                p.insert(a_index+1, b)
                p.pop(b_index)
            # print(p)  # debug

    # 異常チェック
    for ab in ab_list:
        a = ab[0]
        b = ab[1]
        a_index = p.index(a)
        b_index = p.index(b)
        if a_index > b_index:
            print(-1)
            return

    print(' '.join(list(map(str, p))))



if __name__ == '__main__':
    main()
