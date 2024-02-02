T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 수열의 길이
    series = input()
    count = 0
    max_v = 0
    for num in series:
        if int(num) == 1:
            count += 1
        else:
            if max_v < count:
                max_v = count
            count = 0
        if max_v < count:
            max_v = count

    print((f'#{tc} {max_v}'))