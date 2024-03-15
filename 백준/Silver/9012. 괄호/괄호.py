import sys

T = int(input())
for _ in range(T):
    word = sys.stdin.readline()
    que = []
    top = -1
    for w in word:
        if w == '(':
            top += 1
        elif w == ')' and top == -1:
            print('NO')
            break
        elif w == ')':
            top -= 1
    else:
        if top != -1:
            print("NO")
        else:
            print('YES')
