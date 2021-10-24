def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    ans = 0
    i, j = 0, 0  # i: 500円玉を選ぶ枚数、j: 100円玉を選ぶ枚数
    while i <= a and x - 500 * i >= 0:
        rest = x - 500 * i
        while j <= b and rest - 100 * j >= 0:
            rest2 = rest - 100 * j
            if rest2 // 50 <= c:
                ans += 1
            j += 1
        j = 0
        i += 1
    print(ans)


if __name__ == '__main__':
    main()
