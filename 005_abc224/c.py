import math
from fractions import Fraction


def main():
    N = int(input())
    XY = []
    for _ in range(N):
        XY.append(tuple(map(int, input().split())))

    st_cnt = 0  # 直線になるパターン数
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if XY[j][0] - XY[i][0] == 0 and XY[k][0] - XY[i][0] == 0:
                    st_cnt += 1
                elif XY[j][0] - XY[i][0] == 0 or XY[k][0] - XY[i][0] == 0:
                    continue
                else:
                    inc1 = Fraction(XY[j][1] - XY[i][1], XY[j][0] - XY[i][0])
                    inc2 = Fraction(XY[k][1] - XY[i][1], XY[k][0] - XY[i][0])
                    if inc1 == inc2:
                        st_cnt += 1
    all_cnt = N * (N-1) * (N-2) // 6
    # print(all_cnt, ', ', st_cnt)
    print(all_cnt - st_cnt)


if __name__ == '__main__':
    main()
