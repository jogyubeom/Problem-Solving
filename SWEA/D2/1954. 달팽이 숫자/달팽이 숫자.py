T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1] * 100
    dc = [1, 0, -1, 0] * 100
    direction = 0
    arr[0][0] = 1
    r = 0
    c = 0
    for _ in range(N**2 - 1):
        if 0 <= r + dr[direction] <= N-1 and 0 <= c + dc[direction] <= N-1 and \
                arr[r + dr[direction]][c + dc[direction]] == 0:
            arr[r + dr[direction]][c + dc[direction]] = arr[r][c] + 1
            r = r + dr[direction]
            c = c + dc[direction]
        else:
            direction += 1
            arr[r + dr[direction]][c + dc[direction]] = arr[r][c] + 1
            r = r + dr[direction]
            c = c + dc[direction]
    print(f'#{tc}')
    for row in arr:
        print(*row)