def main():
    s = input()

    while len(s) > 0:
        if len(s) < 5:
            print('NO')
            return

        if s[:5] == 'dream':
            if len(s) == 7:
                if s == 'dreamer':
                    print('YES')
                    return
                else:
                    print('NO')
                    return
            elif len(s) > 7 and s[5:7] == 'er':
                if s[7] == 'a':
                    s = s[5:]
                else:
                    s = s[7:]
            else:
                s = s[5:]
        elif s[:5] == 'erase':
            if len(s) >= 6 and s[5] == 'r':
                s = s[6:]
            else:
                s = s[5:]
        else:
            print('NO')
            return
    if len(s) == 0:
        print("YES")


if __name__ == '__main__':
    main()
