def main():
    ss = list(map(int, list(input())))

    cnt = 0
    for s in ss:
        if s == 1:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
