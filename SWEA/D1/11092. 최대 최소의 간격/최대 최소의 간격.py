T = int(input())  # 테스트 케이스
for tc in range(1, 1 + T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = 0
    min_val = 11
    max_idx = -1
    min_idx = -1
    for i in range(N):
        if arr[i] >= max_val:
            max_val = arr[i]
            max_idx = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    print(f'#{tc} {abs(max_idx - min_idx)}')