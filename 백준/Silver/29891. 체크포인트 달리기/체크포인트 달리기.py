N, K = map(int, input().split())
points = []
for _ in range(N):
    points.append(int(input()))
points.sort()
result = 0
while len(points) != 0:
    plus = []
    next1 = points.pop()
    plus.append(abs(next1))
    for _ in range(K-1):
        if len(points) != 0:
            next2 = points.pop()
            if next1 * next2 < 0:
                points.append(next2)
    result += max(plus) * 2
print(result)
