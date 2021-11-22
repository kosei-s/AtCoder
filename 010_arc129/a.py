# xを２進表記した最上位桁だけ見ればいいことに気づけなかった。。
N, L, R = map(int, input().split())

cnt = 0
N_bin = bin(N)[2:]
skip_num = 0
for x in range(L, R+1):
    x_bin = bin(x)[2:]
    diff_fig = len(N_bin) - len(x_bin)
    if diff_fig < 0:
        break
    n_bin = N_bin[diff_fig:]
    for i in range(skip_num, len(x_bin)):
        if n_bin[i] == x_bin[i] and n_bin[i] == '1':
            cnt += 1
            skip_num = 0
            break
        elif n_bin[i] != x_bin[i] and n_bin[i] == '0':
            skip_num = i
            break
        elif i == len(x_bin)-1:
            skip_num = 0
        else:
            continue

print(cnt)
