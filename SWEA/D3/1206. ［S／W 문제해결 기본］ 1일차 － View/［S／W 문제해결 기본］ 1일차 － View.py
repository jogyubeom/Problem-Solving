    # ///////////////////////////////////////////////////////////////////////////////////
for t in range(10):
    N = int(input())    # 빌딩 높이 리스트 길이 (len)
    building_high = list(map(int, input().split()))
    count = 0   # 조망권이 확보된 세대 수
    for num in range(2, N - 2):
        if building_high[num] - building_high[num - 2] > 0 and \
                building_high[num] - building_high[num - 1] > 0 and \
                building_high[num] - building_high[num + 1] > 0 and \
                building_high[num] - building_high[num + 2] > 0:
            count += min(building_high[num] - building_high[num - 2], \
                         building_high[num] - building_high[num - 1], \
                         building_high[num] - building_high[num + 1], \
                         building_high[num] - building_high[num + 2])
    print(f'#{t+1} {count}')

  
    # ///////////////////////////////////////////////////////////////////////////////////
