from re import S


def shift(s: str):
    return s[1:] + s[0]

def main():
    s = input()

    if len(s) == 1:
        print(s)
        print(s)
        return

    s_vars = []  # シフトしてできうる全文字列のリスト
    for i in range(len(s)):
        if i == 0:
            s_vars.append(s)
        else:
            this_s = s
            for j in range(i):
                this_s = shift(this_s)
            s_vars.append(this_s)
    sorted_list = sorted(s_vars)
    print(sorted_list[0])
    print(sorted_list[-1])


if __name__ == '__main__':
    main()
