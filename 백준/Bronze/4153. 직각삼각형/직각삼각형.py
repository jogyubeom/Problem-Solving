arr = list(map(int, input().split()))
while arr[0] != 0:
    arr.sort()
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print('right')
    else:
        print('wrong')
    arr = list(map(int, input().split()))