
N, M, A = map(int, input().split())     # 참가자수, 0모, 자기 번호
me = int(M / 2 + 1)
while True:
    num = int(input())
    if num == me:
        print(0)
        break
    result = A + num - me
    if result <= 0:
        while result <= 0:
            result += N
    elif result > N:
        result %= N
        if result == 0:
            result = N
    print(result)
    A = result

