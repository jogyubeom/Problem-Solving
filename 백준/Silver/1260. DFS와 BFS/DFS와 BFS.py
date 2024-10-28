from collections import deque
# import sys
# sys.stdin = open('input.txt')

def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    go = []
    for n in arr[v]:
        if visited[n] == 0:
            go.append(n)
    if len(go) == 0:
        return
    go.sort()
    for next in go:
        if visited[next]:
            continue
        dfs(next)


def bfs(v):
    que = deque()
    que.append(v)
    while que:
        now = que.popleft()
        print(now, end=' ')
        visited[now] = 1
        go = []
        for n in arr[now]:
            if visited[n] == 0:
                visited[n] = 1
                go.append(n)
        if len(go) == 0:
            continue
        go.sort()
        for next in go:
            que.append(next)
        

N, M, V = map(int, input().split())     # 정점 개수, 간선 개수, 시작 정점
visited = [0] * (N + 1)
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)

