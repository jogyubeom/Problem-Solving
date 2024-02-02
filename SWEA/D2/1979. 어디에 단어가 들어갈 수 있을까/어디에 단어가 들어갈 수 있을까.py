# 가로 또는 세로로 연속한 1의 개수가 k인 경우를 센다.
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)]
    N += 1  # 0인 열과 행을 추가
    ans = 0
    for i in range(N):
        count = 0   # i 행에서 연속한 1의 개수
        for j in range(N):
            if arr[i][j]:
                count += 1
            else:
                if count == K:
                    ans += 1
                count = 0

    for j in range(N):
        count = 0   # j 열에서 연속한 1의 개수
        for i in range(N):
            if arr[i][j]:
                count += 1
            else:
                if count == K:
                    ans += 1
                count = 0
    print((f'#{tc} {ans}'))