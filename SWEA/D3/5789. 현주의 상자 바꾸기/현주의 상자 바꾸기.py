T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())   # N = 상자 개수, Q = 숫자 변경 횟수
    boxes = [0] * N
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        boxes[L-1:R] = [q] * (R-L+1)

    print(f'#{tc}', end=' ')
    print(*boxes)