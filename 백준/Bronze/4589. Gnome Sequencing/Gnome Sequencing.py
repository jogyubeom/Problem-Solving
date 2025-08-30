print("Gnomes:")
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a < b < c:
        print("Ordered")
    elif a > b > c:
        print("Ordered")
    else:
        print("Unordered")