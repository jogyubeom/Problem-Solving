T = int(input())
for tc in range(1, T+1):
    red_box = set()
    blue_box = set()
    N = int(input())
    for n in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        color_box = set()
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                color_box.add((r,c))
        if color == 1 :
            red_box.update(color_box)
        else:
            blue_box.update(color_box)
    count = 0
    for box in red_box:
        if box in blue_box:
            count += 1
    print(f'#{tc} {count}')