for _ in range(int(input())):
    n, m = map(int, input().split())
    if n < 12 or m < 4:
        print(-1)
        continue
    res = 11 * m + 4
    print(res)
        