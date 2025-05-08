import sys
from collections import deque

input = sys.stdin.readline


dy = [-1, 0, 1, 0]  # 상 우 하 좌
dx = [0, 1, 0, -1]
    
N, M = map(int, input().split())
campus = [input() for _ in range(N)]
check = [[0] * M for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start = (i, j)
            check[i][j] = 1

que = deque()
que.append(start)

while que:
    now = que.popleft()
    r = now[0]
    c = now[1]
    for t in range(4):
        nr = r + dy[t]
        nc = c + dx[t]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if check[nr][nc]:
            continue
        if campus[nr][nc] == 'X':
            continue
        if campus[nr][nc] == 'P':
            count += 1
        check[nr][nc] = 1
        que.append((nr, nc))

if count:
    print(count)
else:
    print('TT')