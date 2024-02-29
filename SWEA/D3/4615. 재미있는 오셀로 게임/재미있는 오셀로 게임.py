dr = [-1, 1, 0, 0, -1, -1, 1, 1]     # 상 하 좌 우 좌상 우상 좌하 우하
dc = [0, 0, -1, 1, -1, 1, -1, 1]


T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())    # 보드판 크기, 돌 놓는 횟수
    board = [[0] * N for _ in range(N)]     # 보드판 입력
    board[N//2][N//2] = 'W'
    board[N//2 - 1][N//2] = 'B'
    board[N//2 - 1][N//2 - 1] = 'W'
    board[N//2][N//2 - 1] = 'B'
    count_B = 2
    count_W = 2
    for i in range(M):
        c, r, color = map(int, input().split())     # 좌표, 돌 색깔
        r -= 1
        c -= 1
        if color == 1:
            board[r][c] = 'B'
            count_B += 1
        elif color == 2:
            board[r][c] = 'W'
            count_W += 1
        for t in range(8):
            tmp = []    # 바뀔 수도 있는 것들
            for s in range(1, N):
                nr = r + dr[t] * s
                nc = c + dc[t] * s
                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    break
                if board[nr][nc] == 0:
                    break
                if board[r][c] != board[nr][nc]:
                    tmp.append((nr, nc))
                elif board[r][c] == board[nr][nc]:
                    for rrr in tmp:
                        board[rrr[0]][rrr[1]] = board[r][c]
                    if board[r][c] == 'B':
                        count_B += len(tmp)
                        count_W -= len(tmp)
                    else:
                        count_W += len(tmp)
                        count_B -= len(tmp)
                    break


    print(f'#{tc} {count_B} {count_W}')