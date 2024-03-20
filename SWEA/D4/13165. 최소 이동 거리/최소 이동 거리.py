from collections import deque


def bfs(start, end):
    visited[start] = 1
    distance[start] = 0
    que = deque()
    que.append(start)
    while que:
        now = que.popleft()
        for e, w in road[now]:
            if distance[e] > distance[now] + w:
                distance[e] = distance[now] + w
                que.append(e)


T = int(input())
for tc in range(1, 1+T):
    N, E = map(int, input().split())    # 종점 노드 번호, 간선 개수
    visited = [0] * N   # 노드 방문 표시
    distance = [1e9] * (N+1)  # 출발점에서 해당 노드까지 이동거리
    road = [[] for _ in range(N+1)]     # 각 노드(인덱스)에서 (이동가능한 노드, 거리)\
    for _ in range(E):
        s, e, w = map(int, input().split())
        road[s].append((e, w))
    bfs(0, N)
    print(f'#{tc} {distance[N]}')