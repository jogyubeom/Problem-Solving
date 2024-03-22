def bfs(start):
    q = []
    visited[start] = 1
    depth = 1
    q.append(start)
    while q:
        now = q.pop(0)
        for to in adjl[now]:
            if visited[to]:
                continue
            visited[to] = visited[now] + 1
            q.append(to)


for tc in range(1, 11):
    N, start = map(int, input().split())    # 입력 길이, 시작점
    arr = list(map(int, input().split()))
    visited = [0] * 101     # 방문 표시
    adjl = [[] for _ in range(101)]     # 간선 정보
    for i in range(N//2):
        adjl[arr[2*i]].append(arr[2*i+1])
    bfs(start)
    max_depth = max(visited)
    max_num = 0
    for num in range(101):
        if visited[num] == max_depth:
            max_num = max(max_num, num)
    print(f'#{tc} {max_num}')