from collections import deque
# import sys
# sys.stdin = open('input.txt')

def bfs(v):
    global count
    que = deque()
    que.append(v)
    while que:
        now = que.popleft()
        for n in arr[now]:
            if visited[n] == 0:
                visited[n] = 1
                que.append(n)
        

N, M = map(int, input().split())     # 정점 개수, 간선 개수
visited = [0] * (N + 1)
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
count = 0
for n in range(1, N + 1):
    if visited[n] == 0:
        visited[n] = 1
        count += 1
        bfs(n)
print(count)