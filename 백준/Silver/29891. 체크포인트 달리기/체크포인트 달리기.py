N, K = map(int, input().split())
points = []
points2 = []
for _ in range(N):
    point = int(input())
    if point > 0:
        points.append(point)
    else:
        points2.append(abs(point))
points.sort()
points2.sort()
result = 0
all = [points, points2]
for P in all:
    while len(P) != 0:
        plus = []
        next1 = P.pop()
        result += next1 * 2
        for _ in range(K-1):
            if len(P) != 0:
                P.pop()
print(result)
