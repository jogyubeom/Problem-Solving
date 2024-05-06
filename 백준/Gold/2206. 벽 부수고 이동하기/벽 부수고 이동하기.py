from collections import deque


def bfs(r, c, j):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    que = deque()
    que.append((r, c, j))
    while que:
        r, c, j = que.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][j]
        for t in range(4):
            nr = r + dr[t]
            nc = c + dc[t]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if maze[nr][nc] == 1 and j == 0:
                visited[nr][nc][1] = visited[r][c][0] + 1
                que.append((nr, nc, 1))
            elif maze[nr][nc] == 0 and visited[nr][nc][j] == 0:
                visited[nr][nc][j] = visited[r][c][j] + 1
                que.append((nr, nc, j))
    return -1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

print(bfs(0, 0, 0))