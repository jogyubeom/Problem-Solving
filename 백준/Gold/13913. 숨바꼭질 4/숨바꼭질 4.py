from collections import deque

N, K = map(int, input().split())    # 수빈 위치, 동생 위치
max_n = 100000
visited = list([] for _ in range(max_n + 1))
min_count = 1e9
que = deque()
que.append([N, 0])
while que:
    n, cnt = que.popleft()
    if cnt > min_count:
        continue
    if n == K:
        if cnt <= min_count:
            min_count = min(min_count, cnt)
            print(min_count)
            result = []
            for _ in range(cnt):
                result = visited[K] + result
                [K] = visited[K]
            result += [n]
            print(*result)
            break
    if n-1 >= 0:
        if len(visited[n-1]) == 0:
            que.append([n-1, cnt+1])
            visited[n-1] = [n]
    if n < K and n+1 <= max_n:
        if len(visited[n+1]) == 0:
            que.append([n+1, cnt+1])
            visited[n+1] = [n]
    if n < K and n*2 <= max_n:
        if len(visited[n*2]) == 0:
            que.append([n*2, cnt+1])
            visited[n*2] = [n]
