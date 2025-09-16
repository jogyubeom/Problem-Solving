from math import pi

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

A = a1 / p1
B = pi * r1**2 / p2

if A > B:
    print("Slice of pizza")
    
else:
    print("Whole pizza")