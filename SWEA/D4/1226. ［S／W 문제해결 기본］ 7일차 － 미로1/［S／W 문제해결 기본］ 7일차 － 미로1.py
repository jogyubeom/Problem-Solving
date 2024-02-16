dy = [1, -1, 0, 0]  # 상하좌우
dx = [0, 0, -1, 1]

def bfs(s, g):
    q = []
    visited = [[0] * 16 for _ in range(16)]
    q.append(s)
    visited[s[0]][s[1]] = 1
    while q:
        t = q.pop(0)
        if t == g:
            return 1
        for i in range(4):
            a = t[0] + dy[i]
            b = t[1] + dx[i]
            if 0 <= a < 16 and 0 <= b < 16 and visited[a][b] == 0 and\
                    (maze[a][b] == 0 or maze[a][b] == 3):
                q.append((a,b))
                visited[a][b] = 1 + visited[t[0]][t[1]]
    return 0


for tc in range(1, 11):
    T = int(input())    # 테이스 케이스 번호
    maze = [list(map(int, input())) for _ in range(16)]   # 미로 입력
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                start = (r, c)
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 3:
                end = (r, c)
    result = bfs(start, end)
    print(f'#{tc} {result}')