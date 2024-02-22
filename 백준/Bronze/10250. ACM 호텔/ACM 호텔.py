T = int(input())    # 케이스 번호
for tc in range(1, 1 + T):
    H, W, N = map(int, input().split())     # 호텔 층 수, 각 층의 방 수, 몇 번째 손님
    w = 1   # 방 번호(뒤), 한 자리 수면 앞에 0 붙이기
    num = N
    flag = 0
    while True:
        for _ in range(H):
            num -= 1
            if num == 0:
                flag = 1
                break
        else:
            w += 1
        if flag:
            break

    if w < 10:
        w = '0' + str(w)
    else:
        w = str(w)

    h = N % H  # 방 번호(앞), 0이면 값은 H
    if h == 0:
        h = H
    h = str(h)
    result = int(h + w)
    print(result)