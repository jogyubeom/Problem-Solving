def bfs(s):
    q = []
    visited = [0] * 101
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        for i in adjl[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1 + visited[t]
    return visited

for tc in range(1, 11):
    l, s = map(int, input().split())  # 간선 개수 * 2, 시작점 입력
    line = list(map(int, input().split()))  # 간선 조합들
    adjl = [[] for _ in range(101)]
    for i in range(l // 2):
        n1, n2 = line[i * 2], line[i * 2 + 1]
        adjl[n1].append(n2)
    contact = bfs(s)
    max_v = max(contact)
    my_list = []
    for n in range(101):
        if contact[n] == max_v:
            my_list.append(n)
    result = max(my_list)
    print(f'#{tc} {result}')