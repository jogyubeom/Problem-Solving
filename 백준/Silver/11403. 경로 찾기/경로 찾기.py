import sys
input = sys.stdin.readline

N = int(input())
route = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
visited = [0] * N

def dfs(u, start):
    for v in range(N):
        if route[u][v] == 1:
            if visited[v]:
                continue
            if result[start][v]:
                continue
            visited[v] = 1
            result[start][v] = 1
            dfs(v, start)
            visited[v] = 0

for i in range(N):
    dfs(i, i)

for line in result:
    print(*line)
