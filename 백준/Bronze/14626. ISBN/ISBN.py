import sys
input = sys.stdin.readline

num = input()
temp = 0
for i in range(13):
    if num[i] == '*':
        if i % 2:
            res = 3
        else:
            res = 1
        continue
    if i % 2:
        temp += int(num[i]) * 3
    else:
        temp += int(num[i])

number = 10 - (temp % 10)
if number == 10:
    number = 0
if res == 3:
    while True:
        if number % 3 == 0:
            break
        number += 10
    print(number // 3)
else:
    print(number)
