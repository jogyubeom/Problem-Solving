TC = int(input())
for tc in range(1, 1 + TC):
    N, M, K = map(int, input().split())    # 손님 수, 걸리는 시간, 만들어지는 붕어빵 수
    arrive_time = list(map(int, input().split()))   # 손님들 도착 시간
    count = 0   # 지금까지 판 붕어빵 수
    arrive_time.sort()  # 도착시간 오름차순 정렬
    result = 'Possible'
    for n in range(N):
        if (arrive_time[n] // M * K) - 1 - count < 0:
            result = 'Impossible'
        count += 1
    print(f'#{tc} {result}')