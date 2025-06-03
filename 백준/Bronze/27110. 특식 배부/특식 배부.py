N = int(input())
temp = list(map(int, input().split()))
result = 0
for i in temp:
    if i > N:
        result += N
    else:
        result += i
print(result)