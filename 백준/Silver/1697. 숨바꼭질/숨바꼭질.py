from collections import deque

N, K = map(int, input().split())    # 수빈 위치, 동생 위치
max_n = 100000
visited = [0] * (max_n + 1)
result = 0
que = deque()
que.append([N, 0])
while que:
    n, cnt = que.popleft()
    if n == K:
        result = cnt
        break
    if n-1 >= 0:
        if visited[n-1] == 0:
            que.append([n-1, cnt+1])
            visited[n-1] = 1
    if n < K and n+1 <= max_n:
        if visited[n+1] == 0:
            que.append([n+1, cnt+1])
            visited[n+1] = 1
    if n < K and n*2 <= max_n:
        if visited[n*2] == 0:
            que.append([n*2, cnt+1])
            visited[n*2] = 1
print(result)