A, B, V = map(int, input().split())     # 올라가는 높이, 미끄러지는 높이, 막대 높이
count = 0
count = (V - A)//(A-B) + 1
if (V - A) % (A - B) != 0:
    count += 1
print(count)