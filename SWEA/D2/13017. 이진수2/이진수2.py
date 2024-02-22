T = int(input())
for tc in range(1, 1 + T):
    N = float(input())   # 바꿀 소수 값
    n = 0
    result = ''
    while N != 0:
        n += 1
        if n == 13:
            result = 'overflow'
            break
        val = N // 2**-n
        result += str(int(val))
        N = N - (val * 2**-n)

    print(f'#{tc} {result}')