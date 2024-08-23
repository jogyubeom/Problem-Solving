N = int(input())
S = input()
count = 0
for i in S:
    if i in '1234567890':
        flag = True
        break
else:
    count += 1

for i in S:
    if i.isupper():
        flag = True
        break
else:
    count += 1

for i in S:
    if i.islower():
        flag = True
        break
else:
    count += 1

for i in S:
    if i in '!@#$%^&*()-+':
        flag = True
        break
else:
    count += 1

if N + count < 6:
    count += 6 - N - count

print(count)
