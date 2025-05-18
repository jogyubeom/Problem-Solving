result = 0
for _ in range(2):
    a, b, c, d = map(int, input().split())
    result = max(result, a+b+c+d)
print(result)