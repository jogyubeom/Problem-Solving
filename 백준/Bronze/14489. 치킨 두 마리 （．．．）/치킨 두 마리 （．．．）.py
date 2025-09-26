a, b = map(int, input().split())
m = a + b
chicken = int(input()) * 2
if m >= chicken:
    print(m - chicken)
else:
    print(m)