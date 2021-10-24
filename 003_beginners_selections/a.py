def main():
    inputs = [input() for i in range(3)]
    a = int(inputs[0])
    b = int(inputs[1].split()[0])
    c = int(inputs[1].split()[1])
    s = inputs[2]

    print(f'{a + b + c} {s}')


if __name__ == '__main__':
    main()
