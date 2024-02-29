def exchange(arr, t):
    global max_v
    s = ''.join(arr)
    if s in visited[t]:
        return
    else:
        visited[t].add(s)
    if t == times:
        result = int(''.join(arr))
        max_v = max(result, max_v)
        return
    for i in range(N-1):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
            exchange(arr, t+1)
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())  # 테스트 케이스
for tc in range(1, 1 + T):
    number, times = map(int, input().split())  # 숫자판, 교환 횟수
    number = list(str(number))
    N = len(number)
    visited = [set() for _ in range(11)]
    max_v = 0
    exchange(number, 0)
    print(f'#{tc} {max_v}')