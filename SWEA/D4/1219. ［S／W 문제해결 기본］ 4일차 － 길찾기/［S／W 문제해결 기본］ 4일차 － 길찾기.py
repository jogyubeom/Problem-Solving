def dfs(c, g):
    visited = [0]*(100)
    st = []
    visited[c] = 1
    while True:
        if c == g:
            return 1
        for n in adjl[c]:
            if visited[n] == 0:
                st.append(c)
                c = n
                visited[n] = 1
                break
        else:
            if st:
                c = st.pop()
            else:
                return 0


for _ in range(1, 11):
    T, E = map(int, input().split())  # T = 케이스 번호, E = 간선 개수
    adjl = [[] for _ in range(100)]
    arr = list(map(int, input().split()))   # 경로 순서쌍
    for n in range(E):
        s, g = arr[n * 2], arr[n * 2 + 1]
        adjl[s].append(g)
    result = dfs(0, 99)

    print(f'#{T} {result}')
