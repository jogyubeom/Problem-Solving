N, T = map(int, input().split())
arr = list(range(1, 2 * N + 1)) + list(range(2 * N - 1, 1, -1))
T = (T - 1) % len(arr)
print(arr[T])