

dr = [0, -1, -1, -1, 0, 1, 1, 1]     # 좌부터 좌하까지 8방향
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
word = 'OBIS'

def check(r, c):
    global count
    for t in range(8):
        nr, nc = r, c
        for i in range(4):
            nr += dr[t]
            nc += dc[t]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break
            if board[nr][nc] != word[i]:
                break
        else:
            count += 1


N = int(input())
board = [input() for _ in range(N)]
count = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 'M':
            check(r, c)
print(count)