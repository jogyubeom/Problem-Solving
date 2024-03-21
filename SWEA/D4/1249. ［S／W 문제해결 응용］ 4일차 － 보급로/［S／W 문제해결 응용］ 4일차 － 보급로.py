from collections import deque

dr = [-1, 0, 1, 0]     # 상, 우, 하, 좌
dc = [0, 1, 0, -1]


def bfs(start_r, start_c):
    que = deque()
    que.append((start_r, start_c))
    distance[start_r][start_c] = 0
    while que:
        now_r, now_c = que.popleft()
        for t in range(4):
            new_r = now_r + dr[t]
            new_c = now_c + dc[t]
            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
                continue
            if distance[new_r][new_c] > distance[now_r][now_c] + war_map[new_r][new_c]:
                distance[new_r][new_c] = distance[now_r][now_c] + war_map[new_r][new_c]
                que.append((new_r, new_c))


for tc in range(1, int(input()) + 1):
    N = int(input())    # 지도의 크기
    war_map = [list(map(int, input())) for _ in range(N)]   # 지도
    distance = [[1e9] * N for _ in range(N)]  # 출발지에서 현재 위치까지 메우면서 오는데 걸린 시간
    sr, sc = 0, 0
    er, ec = N-1, N-1
    bfs(sr, sc)
    print(f'#{tc} {distance[N-1][N-1]}')