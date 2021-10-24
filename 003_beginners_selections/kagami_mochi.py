def main():
    n = int(input())
    d_list = []
    for _ in range(n):
        d = int(input())
        if not d in d_list:
            d_list.append(d)

    print(len(d_list))


if __name__ == '__main__':
    main()
