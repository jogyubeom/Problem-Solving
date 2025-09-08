n = int(input())
submit = []
answer = []
for _ in range(n):
    submit.append(input())
for _ in range(n):
    answer.append(input())

res = 0

for i in range(n):
    if submit[i] == answer[i]:
        res += 1
        
print(res)