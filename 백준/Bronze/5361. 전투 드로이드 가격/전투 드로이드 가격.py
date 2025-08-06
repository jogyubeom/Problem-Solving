price = [350.34, 230.90, 190.55, 125.30, 180.90]
for _ in range(int(input())):
    res = 0
    a, b, c, d, e = map(int, input().split())
    res += price[0] * a
    res += price[1] * b
    res += price[2] * c
    res += price[3] * d
    res += price[4] * e
    res = f"{res:.2f}"
    print("$" + res)
    