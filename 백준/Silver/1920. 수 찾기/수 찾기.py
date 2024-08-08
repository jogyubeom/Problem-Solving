N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
num_list.sort()
for i in range(M):
    start = 0
    end = N-1
    found = False
    while start <= end:
        middle = (start + end) // 2
        if num_list[middle] == numbers[i]:
            print(1)
            found = True
            break
        if numbers[i] < num_list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    if found is False:
        print(0)

