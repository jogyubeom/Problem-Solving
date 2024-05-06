from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def burn():
    for _ in range(len(fire)):
        r, c = fire.popleft()
        for t in range(4):
            nr = r + dr[t]
            nc = c + dc[t]
            if 0 <= nr < h and 0 <= nc < w:
                if building[nr][nc] != '#' and building[nr][nc] != '*':
                    building[nr][nc] = '*'
                    fire.append((nr, nc))


def move():
    gogo = False
    for _ in range(len(start)):
        r, c = start.popleft()
        for t in range(4):
            nr = r + dr[t]
            nc = c + dc[t]
            if 0 <= nr < h and 0 <= nc < w:
                if visited[nr][nc] == 0 and building[nr][nc] != '#' and building[nr][nc] != '*':
                    gogo = True
                    visited[nr][nc] = visited[r][c] + 1
                    start.append((nr, nc))
            else:
                return visited[r][c]
    if not gogo:
        return 'IMPOSSIBLE'


T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    arr = []
    fire = deque()
    start = deque()
    building = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire.append((i, j))
            if building[i][j] == '@':
                start.append((i, j))
    visited = [[0] * w for _ in range(h)]
    visited[start[0][0]][start[0][1]] = 1

    result = 0
    while True:
        burn()
        result = move()
        if result:
            break
    print(result)
