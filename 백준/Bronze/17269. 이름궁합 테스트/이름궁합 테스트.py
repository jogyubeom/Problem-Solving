
num = {
    'A':3,
    'B':2,
    'C':1,
    'D':2,
    'E':4,
    'F':3,
    'G':1,
    'H':3,
    'I':1,
    'J':1,
    'K':3,
    'L':1,
    'M':3,
    'N':2,
    'O':1,
    'P':2,
    'Q':2,
    'R':2,
    'S':1,
    'T':2,
    'U':1,
    'V':1,
    'W':1,
    'X':2,
    'Y':2,
    'Z':1,
}

def calculate(W):
    newW = ''
    for i in range(len(W)-1):
        newW += str((int(W[i]) + int(W[i+1])) % 10)
    return newW

N, M = map(int, input().split())
A, B = input().split()
count = 0
word = ''
a = 0
b = 0

while count < N + M:
    if a < N:
        word += A[a]
        a += 1
        count += 1
    if b < M:
        word += B[b]
        b += 1
        count += 1

Numword = ''
for i in word:
    Numword += str(num[i])

while len(Numword) > 2:
    Numword = calculate(Numword)

Numword = str(int(Numword))
print(Numword + '%')
