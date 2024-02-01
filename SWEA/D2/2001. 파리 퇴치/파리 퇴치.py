T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            kill_sum = 0
            for r2 in range(r, r+M):
                for c2 in range(c, c+M):
                    kill_sum += arr[r2][c2]
            sum_list.append(kill_sum)
    result = max(sum_list)
    print(f'#{tc+1} {result}')