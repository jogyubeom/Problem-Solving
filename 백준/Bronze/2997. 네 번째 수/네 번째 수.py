a, b, c = map(int, input().split())
arr = [a, b, c]
arr.sort()
diff = min(arr[1] - arr[0], arr[2] - arr[1])
if arr[1] - arr[0] != diff:
    print(arr[0] + diff)
elif arr[2] - arr[1] != diff:
    print(arr[1] + diff)
else:
    print(arr[2] + diff)