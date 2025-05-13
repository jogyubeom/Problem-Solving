a, b = map(int, input().split())
x = (a + b) // 2
y = a - x
if x < 0 or y < 0:
    print(-1)
elif (a + b) % 2 != 0:
    print(-1)
else:
    print(x, y)