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
        for v in range(1, j + 1):  # i 번째 돌을 사이에 두고 마주보는 j개의 돌에 대해
            if 0 <= i - 1 - v <= N - 1 and 0 <= i - 1 + v <= N - 1:  # 가능한 돌만 작업 진행
                if rock_arr[i - 1 - v] == rock_arr[i - 1 + v]:  # 서로 같은 색이면 뒤집기
                    switch(i - 1 - v)
                    switch(i - 1 + v)
    print(f'#{tc}', end=' ')
    print(*rock_arr)