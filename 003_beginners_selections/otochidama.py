def main():
    n, y = map(int, input().split())

    for i in range(y // 10000 + 1):
        if i == n and 10000 * i == y:
            print(f'{i} 0 0')
            return
        elif i >= n:
            print('-1 -1 -1')
            return

        y2 = y - 10000 * i
        for j in range(y2 // 5000 +1):
            if i + j == n and 5000 * j == y2:
                print(f'{i} {j} 0')
                return
            elif i + j >= n:
                break
            y3 = y2 - 5000 * j
            k = n - (i + j)
            if 1000 * k == y3:
                print(f'{i} {j} {k}')
                return
    print('-1 -1 -1')


if __name__ == '__main__':
    main()
