N = int(input())
for _ in range(N):
    T, t, A, B = map(int, input().split())
    time = t * B
    A -= time // T
    if A <= 0:
        print(time)
        continue
    flag1 = False
    if time % T:
        flag1 = True
        plus = time % T
    flag = False
    if A % 2 != 0:
        flag = True
        A = A // 2 + 1
    else:
        A //= 2
    time += T * A
    if flag and flag1:
            time -= plus
    print(time)