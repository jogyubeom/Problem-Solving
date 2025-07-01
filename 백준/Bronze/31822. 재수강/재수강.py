code = input()[:5]
result = 0
for _ in range(int(input())):
    if code == input()[:5]:
        result += 1
        
print(result)