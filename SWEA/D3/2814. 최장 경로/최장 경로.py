def dfs(now, count):
    global max_count
    flag = False
    for i in graph[now]:
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i, count+1)
        visited[i] = 0
        flag = True
    if not flag:
        max_count = max(max_count, count)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())    # 정점 개수, 간선 개수
    graph = [[] for _ in range(N + 1)]  # 각 정점(인덱스)에서 갈 수 있는 노드들
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    visited = [0] * (N+1)   # 각 정점 방문 표시
    max_count = 0   # 경로 길이 = 등장한 정점 개수
    for n in range(1, N+1):
        visited[n] = 1
        dfs(n, 1)
        visited[n] = 0
    print(f'#{tc} {max_count}')