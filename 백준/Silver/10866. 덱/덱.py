import sys

N = int(input())
deque = []
top = -1
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        deque.insert(0, int(order[1]))
        top += 1
    elif order[0] == 'push_back':
        deque.append(int(order[1]))
        top += 1
    elif order[0] == 'pop_front':
        if top == -1:
            print(-1)
        else:
            print(deque.pop(0))
            top -= 1
    elif order[0] == 'pop_back':
        if top == -1:
            print(-1)
        else:
            print(deque.pop())
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
            print(deque[0])
    elif order[0] == 'back':
        if top == -1:
            print(-1)
        else:
            print(deque[top])
