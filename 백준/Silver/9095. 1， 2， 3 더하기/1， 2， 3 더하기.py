def check(num):
    global count
    for n in range(1, 4):
        next = num - n
        if next == 0:
            count += 1
            continue
        elif next < 0:
            continue
        check(next)


T = int(input())
for _ in range(T):
    count = 0
    n = int(input())
    check(n)
    print(count)