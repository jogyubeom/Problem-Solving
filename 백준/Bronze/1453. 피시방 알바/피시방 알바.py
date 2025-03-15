N = int(input())
numbers = list(map(int, input().split()))
checkList = [0] * 101
result = 0
for i in numbers:
    if checkList[i] == 0:
        checkList[i] = 1
    else:
        result += 1
print(result)
