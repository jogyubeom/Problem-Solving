import sys
from collections import deque

input = sys.stdin.readline


dy = [-1, 0, 1, 0]  # 상 우 하 좌
dx = [0, 1, 0, -1]
    
N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]

que = deque()
que.append((0, 0))
campus[0][0] = 1

while que:
    now = que.popleft()
    r = now[0]
    c = now[1]
    for t in range(4):
        nr = r + dy[t]
        nc = c + dx[t]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if campus[nr][nc] == '0':
            continue
        if campus[nr][nc] == '1':
            campus[nr][nc] = campus[r][c] + 1
            que.append((nr, nc))

print(campus[N-1][M-1])