T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(float, input().split())   # D = 기차 간 거리, AB = 기차 속력, F = 파리 속력
    time = D / (A + B)
    result = F * time

    print(f'#{tc} {result}')