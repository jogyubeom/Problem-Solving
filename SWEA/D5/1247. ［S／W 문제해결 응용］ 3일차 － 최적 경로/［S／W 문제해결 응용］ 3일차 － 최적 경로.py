def route_search(v, s, pre):  # 최단 경로 구하기
    global min_val
    if v == N + 1:
        visited[1] = 1
        s += abs(loca[pre][0] - loca[1][0]) + abs(loca[pre][1] - loca[1][1])
        if min_val > s:
            min_val = s
        return
    elif s > min_val:
        return
    for n in range(2, N + 2):
        if visited[n]:
            continue
        visited[n] = 1
        route_search(v + 1, s + abs(loca[pre][0]-loca[n][0]) + abs(loca[pre][1]-loca[n][1]), n)
        visited[n] = 0


T = int(input())  # 테스트 케이스
for tc in range(1, 1 + T):
    N = int(input())  # 고객의 수
    loca = []
    arr = list(map(int, input().split()))
    for i in range(N+2):
        x, y = arr[i * 2], arr[i * 2 + 1]
        loca.append((x, y))     # [0]=회사, [1]=집, [2]...=고객
    visited = [0] * (N + 2)  # 방문 표시할 리스트
    visited[0] = 1  # 회사에서 출발
    min_val = 9999999
    route_search(1, 0, 0)
    print(f'#{tc} {min_val}')
