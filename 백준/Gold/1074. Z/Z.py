N, r, c = map(int, input().split())

def track(n, x, y, res):
    if n == 1:
        res += 2 * x + y
        print(res)
        return
    
    half = 2**(n - 1)

    if x < half and y < half:   # 1사분면
        track(n-1, x, y, res)

    elif x < half and y >= half: # 2사분면
        track(n-1, x, y - half, res + half**2)

    elif x >= half and y < half: # 3사분면
        track(n-1, x - half, y, res + 2 * half**2)
    
    else:
        track(n-1, x - half, y - half, res + 3 * half**2)


track(N, r, c, 0)