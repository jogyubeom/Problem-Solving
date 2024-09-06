import sys

N = int(input())
jinjuWage = 0
wages = [0] * 1001
count = 0
for _ in range(N):
    depart, wage = sys.stdin.readline().split()
    wage = int(wage)
    if depart == 'jinju':
        jinjuWage = wage
    if wage > 1000:
        count += 1
    else:
        wages[wage] += 1
count += sum(wages[jinjuWage + 1 :])
print(jinjuWage)
print(count)