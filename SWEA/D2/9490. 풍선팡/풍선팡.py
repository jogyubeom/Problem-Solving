T = int(input())
for tc in range(T):
    N, M = map(int, input().split())    # N = 행 개수 , M = 풍선 개수 = 열 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]  # 우 하 좌 상
    dc = [1, 0, -1, 0]
    flower_spread = []
    for r in range(N):
        for c in range(M):
            sum = arr[r][c]
            for i in range(4):
                for s in range(1, arr[r][c] + 1):
                    nr = r + dr[i] * s
                    nc = c + dc[i] * s
                    if 0 <= nr <= N-1 and 0 <= nc <= M-1:
                        sum += arr[nr][nc]
            flower_spread.append(sum)
    result = max(flower_spread)
    print(f'#{tc+1} {result}')