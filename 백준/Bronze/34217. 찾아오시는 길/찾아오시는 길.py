a, b = map(int, input().split())
c, d = map(int, input().split())
h = a + c
y = b + d
if h < y:
    print("Hanyang Univ.")
elif h == y:
    print("Either")
else:
    print("Yongdap")