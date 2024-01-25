N, X = input().split()
A = input().split()
N = int(N)

for n in range(N):
    if int(A[n]) < int(X):
        print(int(A[n]), end=' ')