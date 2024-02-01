def dump(num_list):
    high_num = 0    # 가장 높은 상자 높이
    high_index = 0  # 가장 높은 상자 인덱스
    low_num = 100    # 가장 낮은 상자 높이
    low_index = 0   # 가장 낮은 상자 인덱스
    for n in range(100):
        if num_list[n] > high_num:
            high_num = num_list[n]
            high_index = n
        if num_list[n] < low_num:
            low_num = num_list[n]
            low_index = n
    num_list[high_index] -= 1
    num_list[low_index] += 1
    return num_list

def high_low(num_list):
    high_num = 0    # 가장 높은 상자 높이
    low_num = 100    # 가장 낮은 상자 높이
    for n in range(100):
        if num_list[n] > high_num:
            high_num = num_list[n]
        if num_list[n] < low_num:
            low_num = num_list[n]
    return high_num - low_num

for t in range(1, 11):
    N = int(input())
    height_list = list(map(int, input().split()))
    for _ in range(N):
        height_list = dump(height_list)
    result = high_low(height_list)
    print(f'#{t} {result}')
