def cycle(N):
    if N < 10:
        a = 0
        b = N
    elif N >= 10:
        a = N // 10
        b = N % 10
    count = 0
    while True:
        na = b
        nb = (a + b) % 10
        count += 1
        if na * 10 + nb == N:
            break
        a = na
        b = nb
    return count

N = int(input())
print(cycle(N))