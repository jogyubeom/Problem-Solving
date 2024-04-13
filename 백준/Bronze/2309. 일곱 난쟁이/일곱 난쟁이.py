
kids = []
goal = 0
for _ in range(9):
    height = int(input())
    kids.append(height)
    goal += height
goal -= 100     # 제외한 2명 키 합
one = -1e9
two = -1e9
kids.sort()
for i in range(8):
    if one + two > 0:
        break
    for j in range(i+1, 9):
        if kids[i] + kids[j] == goal:
            one = i
            two = j
            break
for n in range(9):
    if n == one or n == two:
        continue
    print(kids[n])
