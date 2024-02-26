T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    card_list = input().split()
    a = 0
    b = (N + 1) // 2
    print(f'#{tc}', end=' ')
    for turn in range(N):
        if turn % 2 == 0:
            print(card_list[a], end=' ')
            a += 1
        else:
            print(card_list[b], end=' ')
            b += 1
    print()