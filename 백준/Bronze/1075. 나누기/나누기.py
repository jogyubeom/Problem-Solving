N = int(input())
F = int(input())
n = N % 100
N -= n

while True:
    if N % F == 0:
        break
    N += 1

print(str(N)[-2] + str(N)[-1])
