TC = int(input())
for tc in range(1, 1 + TC):
    N, T = map(int, input().split())    # 카드의 개수, 셔플 횟수
    card_arr = list(range(1, N+1))
    for i in range(T):
        overhand = N * 37 // 100
        for _ in range(overhand):
            card_arr.insert(0, card_arr.pop())
        a = 0
        b = (N+1) // 2
        new_arr = []
        for turn in range(N):
            if turn % 2 == 0:
                new_arr.append(card_arr[a])
                a += 1
            else:
                new_arr.append(card_arr[b])
                b += 1
        card_arr = new_arr
    print(f'#{tc}', end=' ')
    print(*card_arr)