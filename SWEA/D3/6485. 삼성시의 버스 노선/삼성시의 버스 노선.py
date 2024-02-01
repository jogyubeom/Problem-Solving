def bus_check(bus_route, stop):
    count = 0
    for route in bus_route:
        if route[0] <= stop <= route[1]:
            count += 1
    return count

T = int(input())
for tc in range(T):
    N = int(input())    # 버스 노선 개수
    bus_route = []
    for _ in range(N):  # 버스 노선 입력 (리스트 형태)
        a,b = map(int, input().split())
        bus_route.append([a,b])
    P = int(input())    # 버스 정류장 개수
    bus_stop = []
    for _ in range(P):  # 버스 정류장 입력 (리스트의 원소)
        c = int(input())
        bus_stop.append(c)
    result = []
    for b in bus_stop:
        result.append(bus_check(bus_route, b))

    print(f'#{tc+1}',end=' ')
    print(*result)