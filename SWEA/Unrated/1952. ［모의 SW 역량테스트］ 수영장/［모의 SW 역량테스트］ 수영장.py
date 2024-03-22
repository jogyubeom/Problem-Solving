from collections import deque


def bfs(month, sum_cost):
    global min_cost
    que = deque()
    que.append((month, sum_cost))
    while que:
        now, c = que.popleft()
        if c > min_cost:
            continue
        if now >= 12:
            min_cost = min(min_cost, c)
            continue
        que.append((now+1, c + cost[0] * calender[now]))
        if calender[now] != 0:
            que.append((now+1, c + cost[1]))
        que.append((now+3, c + cost[2]))


T = int(input())
for tc in range(1, T + 1):
    cost = list(map(int, input().split()))  # 이용권 요금
    calender = list(map(int, input().split()))  # 1년 이용계획
    min_cost = 1e9
    bfs(0, 0)
    min_cost = min(min_cost, cost[3])
    print(f'#{tc} {min_cost}')