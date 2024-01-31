T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    P = ''
    for s in S:
        P = P + (s * R)
    print(P)