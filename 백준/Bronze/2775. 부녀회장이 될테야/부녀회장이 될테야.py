
T = int(input())  # 테스트 케이스
for tc in range(1, 1 + T):
    K = int(input())    # 층
    n = int(input())    # 호
    zero_floor = [x for x in range(1, n+1)]
    for _ in range(K):
        for i in range(1, n):
            zero_floor[i] += zero_floor[i-1]
    print(zero_floor[n-1])
