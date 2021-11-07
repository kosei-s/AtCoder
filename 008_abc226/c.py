# これだといくたか実行時エラーとなった。（なぜ？）
# 解説見るともっとシンプルな方法存在した。。
N = int(input())
T = []
K = []
AA_tmp = []
for _ in range(N):
    inputs = list(map(int, input().split()))
    T.append(inputs[0])
    K.append(inputs[1])
    AA_tmp.append(inputs[2:])
AA = []
for A_tmp in AA_tmp:
    AA.append(list(map(lambda x: x-1, A_tmp)))

checked = []

def calc_time(skill: int) -> int:
    global checked
    tmp_time = 0
    check_A_list = [a for a in AA[skill] if a not in checked]
    checked += check_A_list
    check_A_list.sort()
    # print(check_A_list)
    for a in check_A_list:
        tmp_time += calc_time(a)
    return tmp_time + T[skill]

def main():
    print(calc_time(N-1))

if __name__ == '__main__':
    main()
