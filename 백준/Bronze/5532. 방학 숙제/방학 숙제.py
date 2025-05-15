L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

one = A // C
if A % C != 0:
    one += 1

two = B // D
if B % D != 0:
    two += 1

result = L - max(one, two)
print(result)