now = int(input()) 
end = int(input())
minus = int(input())
ice = int(input())
plus = int(input())
time = 0
check = 0

while True:
    if now == end:
        print(time)
        break
    if now < 0:
        time += minus * (now) * -1
        now = 0
    elif now == 0 and check == 0:
        time += ice
        check = 1
    else:
        if now <= 0:
            time += plus * end
        else:
            time += plus * (end - now)
        now = end
        