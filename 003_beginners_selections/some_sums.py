def main():
    n, a, b = map(int, input().split())

    ans = 0
    for i in range(n):
        i += 1
        total = sum(map(int, list(str(i))))
        if a <= total <= b:
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
