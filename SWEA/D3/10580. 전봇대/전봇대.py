def comb(v):
    global count
    if v == N-1:
        return
    for i in range(v+1, N):
        if (A[v] - A[i]) * (B[v] - B[i]) < 0:
            count += 1
    comb(v+1)
    return 


TC = int(input())
for tc in range(1, 1+TC):
    N = int(input())
    A = []
    B = []
    count = 0
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    comb(0)
    print(f'#{tc} {count}')