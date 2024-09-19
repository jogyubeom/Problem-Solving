
count = 1
while True:
    N = int(input())
    if N == 0:
        break
    M = 0
    for i in range(1, 9):
        if N >= 5**i:
            M += N // 5**i
        else:
            break
    print(f'Case #{count}: {M}')
    count += 1
