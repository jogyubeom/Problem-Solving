n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if i == 300:
        print(1, end=" ")
    elif 300 > i >= 275:
        print(2, end=" ")
    elif 275 > i >= 250:
        print(3, end=" ")
    else:
        print(4, end=" ")
        