for _ in range(int(input())):
    a, b = input().split()
    a = float(a)
    if b == 'kg':
        print(f'{round(a * 2.2046, 4):.4f}', 'lb')
    elif b == 'lb':
        print(f'{round(a * 0.4536, 4):.4f}', 'kg')
    elif b == 'l':
        print(f'{round(a * 0.2642, 4):.4f}', 'g')
    else:
        print(f'{round(a * 3.7854, 4):.4f}', 'l')