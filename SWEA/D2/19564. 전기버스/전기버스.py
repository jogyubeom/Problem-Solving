def charging(a,b,charge_M):
    charging_point = []
    for i in charge_M:
        if a < i <= b:
            charging_point.append(i)
    if len(charging_point) >= 1:
        return max(charging_point)
    else:
        return False

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_M = list(map(int, input().split()))
    count = 0   # 충전 횟수
    current_point = 0   # 버스 위치
    while True:
        current_point += K
        if current_point < N:
            reply = charging(current_point-K, current_point, charge_M)
            if reply is False:
                count = 0
                break
            current_point = reply
            count += 1
        elif current_point >= N:
            break
    print(f'#{t} {count}')