d, h, m = map(int, input().split())
temp = 0

temp += (d - 11) * 24 * 60
    
temp += (h - 11) * 60

temp += (m - 11)

if temp < 0:
    print(-1)
else:
    print(temp)