import sys

N = int(input())
que = []
top = -1
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        que.append(int(order[1]))
        top += 1
    elif order[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(que.pop(0))
            top -= 1
    elif order[0] == 'size':
        print(top+1)
    elif order[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if top == -1:
            print(-1)
        else:
            print(que[0])
    elif order[0] == 'back':
        if top == -1:
            print(-1)
        else:
            print(que[top])
