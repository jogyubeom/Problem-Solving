for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = set()
    for r in range(100):
        sum_1 = 0
        for c in range(100):
            sum_1 += arr[r][c]
            sum_list.add(sum_1)
    for c in range(100):
        sum_2 = 0
        for r in range(100):
            sum_2 += arr[r][c]
            sum_list.add(sum_2)
    for r in range(100):
        sum_3 = 0
        sum_3 += arr[r][r]
        sum_list.add(sum_3)
    for r in range(100):
        sum_4 = 0
        sum_4 += arr[r][99-r]
        sum_list.add(sum_4)
    result = max(sum_list)
    print(f'#{tc} {result}')
