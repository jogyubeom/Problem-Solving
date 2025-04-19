import sys
input = sys.stdin.readline

from collections import deque

dy = [-1, 0, 1, 0]  # 상 우 하 좌
dx = [0, 1, 0, -1]
    
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
check_dist = [[0] * m for _ in range(n)]
res = 0

def dfs(r, c, num, count):
    global res

    if count != 4:

        for t in range(4):  # 이동
            nr = r + dy[t]
            nc = c + dx[t]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if check_dist[nr][nc] == 1:
                continue
            check_dist[nr][nc] = 1
            dfs(nr, nc, num + grid[nr][nc], count + 1)
            check_dist[nr][nc] = 0
    
    else:
        res = max(res, num)


for i in range(n):
    for j in range(m):
        check_dist[i][j] = 1
        dfs(i, j, grid[i][j], 1)
        check_dist[i][j] = 0
        numbers = []
        for t in range(4):  # 이동
            nr = i + dy[t]
            nc = j + dx[t]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            numbers.append(grid[nr][nc])
        if len(numbers) == 4:
            numbers.sort(reverse=True)
            numbers.pop()
            res = max(res, grid[i][j] + sum(numbers))
        elif len(numbers) == 3:
            res = max(res, grid[i][j] + sum(numbers))

print(res)