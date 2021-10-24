def calc_p(a: int):
    p = 0
    while a % 2 == 0:
        p += 1
        a = a // 2
    return p


def main():
    n = int(input())
    a_list = map(int, input().split())

    p_list = []  # 各Aを素因数分解したときに2の何乗の数値
    for a in a_list:
        p_list.append(calc_p(a))
    print(min(p_list))


if __name__ == '__main__':
    main()
