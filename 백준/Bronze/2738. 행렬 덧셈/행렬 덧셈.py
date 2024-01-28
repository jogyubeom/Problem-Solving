N, M = map(int,input().split())
A = []
for n in range(N):
    A.append(list(map(int,input().split())))

B = []
for n in range(N):
    B.append(list(map(int,input().split())))

S = []
for n in range(N):
    for i in range(M):
        S.append(A[n][i] + B[n][i])

for n in range(N):
    for i in range(M):
        print(S.pop(0),end=' ')
    print()