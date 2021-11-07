X = input()

int_part = int(X.split('.')[0])
first_dicimal = int(X.split('.')[1][0])

if first_dicimal >= 5:
    print(int_part+1)
else:
    print(int_part)
