
import sys
input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))
check = dict()
left = 0
result = 0

for right in range(N):
    if fruits[right] in check:
        check[fruits[right]] += 1
    else:
        check[fruits[right]] = 1
    
    while len(check) > 2:
        check[fruits[left]] -= 1
        if check[fruits[left]] == 0:
            del check[fruits[left]]
        
        left += 1

    result = max(result, right - left + 1)

print(result)
