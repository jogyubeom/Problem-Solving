import sys
input = sys.stdin.readline

from collections import deque

dy = [-1, 0, 1, 0]  # 상 우 하 좌좌
dx = [0, 1, 0, -1]
    
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
check_dist = [[0] * m for _ in range(n)]
flag = False

for i in range(n):
    if flag:
        break
    for j in range(m):
        if map[i][j] == 2:
            start = (i, j, 0)
            flag = True
            break

que = deque()
que.append(start)

while que:
    now = que.popleft()
    y = now[0]
    x = now[1]
    dist = now[2]
    for t in range(4):  # 이동
        ny = y + dy[t]
        nx = x + dx[t]
        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        if map[ny][nx] == 0 or map[ny][nx] == 2:
            continue
        if check_dist[ny][nx] == 0 or dist + 1 < check_dist[ny][nx]:
            check_dist[ny][nx] = dist + 1
            que.append((ny, nx, dist + 1))

for i in range(n):
    for j in range(m):
        if check_dist[i][j] == 0 and map[i][j] == 1:
            check_dist[i][j] = -1

for i in range(n):
    print(*check_dist[i])