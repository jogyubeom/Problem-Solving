from collections import deque


def bfs(start, height):
    global min_height
    que = deque()
    que.append((start, height))     # 현재 직원, 현재 탑 높이
    while que:
        now, sum_h = que.popleft()
        if now == N:
            if sum_h >= B:
                min_height = min(min_height, sum_h)
            continue
        if sum_h > min_height:
            continue
        que.append((now+1, sum_h + arr[now]))
        que.append((now+1, sum_h))


T = int(input())
for tc in range(1, 1+T):
    N, B = map(int, input().split())    # 직원 수, 선반 높이
    arr = list(map(int, input().split()))   # 직원들 키
    min_height = 1e9
    bfs(0, 0)
    print(f'#{tc} {min_height - B}')