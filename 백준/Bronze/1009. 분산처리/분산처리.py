for _ in range(int(input())):
    a, b = map(int, input().split())
    a = a % 10
    if a in [1, 5, 6, 0]:
        if a == 0:
            print(10)
        else:
            print(a)
    elif a in [4, 9]:
        b = b % 2
        if b == 0:
            b = 2
        print(a**b%10)
    else:
        b = b % 4
        if b == 0:
            b = 4
        print(a**b%10)
