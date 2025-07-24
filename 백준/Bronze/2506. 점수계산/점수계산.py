n = int(input())
sol = list(map(int, input().split()))
check = 0
res = 0
for s in sol:
    if s:
        check += 1
        res += check
    else:
        check = 0
        
print(res)