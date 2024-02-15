r, c = map(int, input().split())    # 가로, 세로 입력
t = int(input())
raw = [0, r]    # 가로
col = [0, c]    # 세로
for _ in range(t):
    n, val = map(int, input().split())    # 가로/세로, 번호
    if n == 0:
        col.append(val)
    else:
        raw.append(val)
raw.sort()
col.sort()
size_list = []
width = []
height = []
for n in range(1, len(raw)):
    width.append(raw[n] - raw[n-1])
for n in range(1, len(col)):
    height.append(col[n] - col[n-1])

for w in width:
    for h in height:
        size_list.append(w * h)

print(max(size_list))