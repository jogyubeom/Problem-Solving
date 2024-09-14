import sys
input = sys.stdin.readline

S = [0] * 21

def add(x):
    S[x] = 1

def remove(x):
    if S[x] == 1:
        S[x] = 0

def check(x):
    if S[x] == 1:
        print(1)
    else:
        print(0)

def toggle(x):
    if S[x] == 1:
        S[x] = 0
    else:
        S[x] = 1

def all():
    for i in range(1, 21):
        S[i] = 1

def empty():
    for i in range(1, 21):
        S[i] = 0

for _ in range(int(input())):
    W = input().split()
    if W[0] == 'all':
        all()
    elif W[0] == 'empty':
        empty()
    else:
        word, num = W[0], W[1]
        num = int(num)
        if word == 'add':
            add(num)
        elif word == 'remove':
            remove(num)
        elif word == 'check':
            check(num)
        elif word == 'toggle':
            toggle(num)
    