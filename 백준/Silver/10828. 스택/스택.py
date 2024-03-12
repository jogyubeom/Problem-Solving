import sys

N = int(input())
stack = []
top = -1
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(int(order[1]))
        top += 1
    elif order[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif order[0] == 'size':
        print(top+1)
    elif order[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])