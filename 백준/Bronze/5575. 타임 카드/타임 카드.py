for _ in range(3):
    h, m, s, hh, mm, ss = map(int, input().split())
    hh -= h
    mm -= m
    ss -= s
    if mm < 0:
        hh -= 1
        mm += 60
    if ss < 0:
        if mm != 0:
            mm -= 1
        else:
            hh -= 1
            mm += 59
        ss += 60
    print(hh, mm, ss)