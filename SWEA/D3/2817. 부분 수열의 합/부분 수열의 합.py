def dfs(n, s, f):
    global count
    if s == K:
        count += 1
        return
    for i in range(f, N):
        if visited[i] != 0:
            continue
        visited[i] = 1
        dfs(n+1, s+arr[i], i+1)
        visited[i] = 0


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())    # 자연수 개수, 합
    arr = list(map(int, input().split()))   # N개 자연수 리스트
    count = 0
    visited = [0] * N
    dfs(0, 0, 0)
    print(f'#{tc} {count}')
