from collections import deque

dr = [-1, -2, -2, -1, 1, 2, 2, 1]     # 좌상하 부터 시계방향으로
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(input())
for _ in range(T):
    I = int(input())    # 체스판 한 변의 길이
    R, C = map(int, input().split())    # 현재 위치
    LR, LC = map(int, input().split())    # 목표 위치

    board = [[0] * I for _ in range(I)]
    board[LR][LC] = 2

    board[R][C] = 1
    que = deque()
    que.append((R, C, 0))
    min_count = 1e9

    if R == LR and C == LC:
        min_count = 0
    else:
        while que:
            current_r, current_c, count = que.popleft()
            if count >= min_count:
                continue
            for t in range(8):
                nr = current_r + dr[t]
                nc = current_c + dc[t]
                if nr < 0 or nr >= I or nc < 0 or nc >= I:
                    continue
                if board[nr][nc] == 1:
                    continue
                if board[nr][nc] == 2:
                    count += 1
                    min_count = count
                    continue
                board[nr][nc] = 1
                que.append((nr, nc, count+1))

    print(min_count)