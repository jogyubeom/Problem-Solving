
def dfs(i, n, num):
    global max_result, min_result
    if i == N-1:
        max_result = max(max_result, num)
        min_result = min(min_result, num)
        return
    for t in range(4):
        if cal[t] == 0:
            continue
        cal[t] -= 1
        if t == 0:
            dfs(i+1, n+1, num + numbers[n])
        elif t == 1:
            dfs(i+1, n+1, num - numbers[n])
        elif t == 2:
            dfs(i+1, n+1, num * numbers[n])
        elif t == 3:
            dfs(i+1, n+1, int(num / numbers[n]))
        cal[t] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 숫자 개수
    cal = list(map(int, input().split()))   # 연산자 개수 (+, -, *, /)
    numbers = list(map(int, input().split()))
    max_result = -1e9
    min_result = 1e9
    dfs(0, 1, numbers[0])

    print(f'#{tc} {max_result - min_result}')
