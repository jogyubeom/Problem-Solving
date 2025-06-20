target = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if target == a:
        target = b
    elif target == b:
        target = a
        
print(target)
        