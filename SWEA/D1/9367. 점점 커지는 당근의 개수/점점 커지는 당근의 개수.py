T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 당근 개수
    series = list(map(int, input().split()))    # 수확한 당근 크기들
    count = 1
    max_v = 1
    for n in range(1, N):
        if series[n-1] < series[n]:
            count += 1
        else:
            if max_v < count:
                max_v = count
            count = 1
        if max_v < count:
            max_v = count

    print((f'#{tc} {max_v}'))