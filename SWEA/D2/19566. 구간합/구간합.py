T = int(input())
for test_case in range(1, T + 1):
    N, M = input().split()
    N = int(N)
    M = int(M)
    arr = list(map(int, input().split()))
    max_sum = 0
    min_sum = 0
    for i in range(M):
        min_sum += arr[i]
    for n in range(N-M+1):
        case_sum = arr[n]
        for j in range(1, M):
            case_sum += arr[n+j]
        if case_sum > max_sum:
            max_sum = case_sum
        if case_sum < min_sum:
            min_sum = case_sum
    result = max_sum - min_sum
    print(f'#{test_case} {result}')
