N = int(input())
A = list(map(int, input().split()))
numbers = set(A)
numbers = list(numbers)
numbers.sort()
P = [0] * N
count = 0
for n in numbers:
    for i in range(N):
        if A[i] == n:
            P[i] = count
            count += 1
            
print(*P)