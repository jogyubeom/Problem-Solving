import math


def is_prime(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    else:
        return True


T = int(input())
for _ in range(T):
    n = int(input())
    current = n
    if current == 0 or current == 1:
        print(2)
        continue
    while True:
        if is_prime(current):
            print(current)
            break
        current += 1
