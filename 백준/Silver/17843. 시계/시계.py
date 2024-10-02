
T = int(input())
for _ in range(T):
    h, m, s = map(int, input().split())
    min_value = 1e9
    result = []
    seconds = 3600 * h + 60 * m + s
    result.append(seconds * (1/120))
    result.append((seconds * 0.1) % 360)
    result.append((seconds * 6) % 360)
    for i in range(3):
        res = abs(result[i] - result[i-1])
        min_value = min(min_value, res, 360-res)
    print(min_value)