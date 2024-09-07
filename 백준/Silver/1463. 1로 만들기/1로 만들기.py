count = [0] * (10**6 + 1)
count[1], count[2], count[3] = 0, 1, 1
N = int(input())
for i in range(4, N+1):
    result = []
    if i % 2 == 0:
        result.append(count[i//2] + 1)
    if i % 3 == 0:
        result.append(count[i//3] + 1)
    result.append(count[i-1] + 1)
    count[i] = min(result)
print(count[N])