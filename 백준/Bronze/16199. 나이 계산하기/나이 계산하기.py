y, m, d = map(int, input().split())
yy, mm, dd = map(int, input().split())

if yy > y:
    if mm > m or (mm == m and dd >= d):
        print(yy - y)
    else:
        print(yy - y - 1)
else:
    print(0)

print(yy - y + 1)
print(yy - y)