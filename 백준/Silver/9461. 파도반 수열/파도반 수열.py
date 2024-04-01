def find(x):
    if x <= 10:
        return arr[x-1]
    else:
        result = find(x-2) + find(x-3)
        return result


T = int(input())
arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10, 100):
    new = arr[i-2] + arr[i-3]
    arr.append(new)
for tc in range(T):
    N = int(input())
    print(arr[N-1])