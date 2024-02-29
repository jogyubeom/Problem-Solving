def switch(r):  # r+1 번째 돌을 뒤집기
    if rock_arr[r] == 0:
        rock_arr[r] = 1
    else:
        rock_arr[r] = 0


T = int(input())    # 테스트 케이스 개수
for tc in range(1, 1+T):
    N, M = map(int, input().split())    # N = 돌의 개수, M = 뒤집기 작업의 총 횟수
    rock_arr = list(map(int, input().split()))  # 돌의 초기 상태
    for _ in range(M):  # M 번의 작업을 진행
        i, j = map(int, input().split())   # i=기준 위치, j=작업할 돌 개수
        for v in range(i - 1, i + j - 1):  # i 번째부터 j개의 돌을 i번째 돌처럼 만들기
            if 0 <= v <= N - 1:  # 가능한 돌만 작업 진행
                rock_arr[v] = rock_arr[i - 1]
    print(f'#{tc}', end=' ')
    print(*rock_arr)