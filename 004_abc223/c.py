def main():
    n = int(input())
    ab_list = []
    for i in range(n):
        ab_list.append(list(map(int, input().split())))

    # 全部燃えるのに何秒かかるか
    x = 0
    y_list = []  # 各導線が燃えるのにそれぞれ何秒かかるか
    for i in range(n):
        y = ab_list[i][0] / ab_list[i][1]
        y_list.append(y)
        x += y
    x = x / 2

    # 答えの算出
    y_sum = 0.0
    ans = 0.0
    for i in range(n):
        y_sum_before = y_sum
        y_sum += y_list[i]
        if y_sum >= x:
            ans += ab_list[i][1] * (x - y_sum_before)
            break
        ans += ab_list[i][0]
    print(ans)


if __name__ == '__main__':
    main()
