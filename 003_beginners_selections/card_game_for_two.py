def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    a_score = 0
    b_score = 0
    for i in range(n):
        current_max = max(a_list)
        if i % 2 == 0:
            a_score += current_max
        else:
            b_score += current_max
        a_list.remove(current_max)
    
    print(a_score - b_score)



if __name__ == '__main__':
    main()
