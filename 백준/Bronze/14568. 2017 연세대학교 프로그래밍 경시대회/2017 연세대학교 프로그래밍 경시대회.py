
N = int(input())    # 사탕 총 개수
count = 0
for A in range(1, N):   # 남규
    for B in range(1, N):   # 영훈
        for C in range(1, N):   # 택희
            if A + B + C != N:
                continue
            if A - B < 2:
                continue
            if A * B * C == 0:
                continue
            if C % 2 != 0:
                continue
            count += 1
print(count)
