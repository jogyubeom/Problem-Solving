direction = []  # 동서남북 : 1234
dist = []
K = int(input())    # 1m**2 당 참외 개수
for _ in range(6):
    a, b = map(int, input().split())
    direction.append(a)     # 방향
    dist.append(b)          # 거리
row = []
col = []
smallRow = 0
smallCol = 0
for i in range(6):
    if direction[i] in [1, 2]:
        row.append(dist[i])
        if direction[i-1] == direction[(i+1) % 6]:
            smallRow = dist[i]
    elif direction[i] in [3, 4]:
        col.append(dist[i])
        if direction[i-1] == direction[(i+1) % 6]:
            smallCol = dist[i]
big = max(row) * max(col)
small = smallRow * smallCol
print((big-small) * K)