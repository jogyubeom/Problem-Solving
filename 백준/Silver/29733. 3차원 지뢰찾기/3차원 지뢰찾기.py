R,C,H= map(int,input().split())
box = []
for i in range (0,H):
    box_lev = []
    for j in range (0,R):
        a = list(input())
        box_lev.append(a)
    box.append(box_lev)

ans = [[[0 for _ in range (0,C)] for _ in range (0,R)] for _ in range (0,H)]
for i in range (0,H):
    for j in range (0,R):
        for k in range (0,C):
            if box[i][j][k] == "*":
                ans[i][j][k] = "*"
            else:
                cnt = 0
                for a in (-1,0,1):
                    for b in (-1,0,1):
                        for c in (-1,0,1):
                            x = i + a
                            y = j + b
                            z = k + c
                            if 0 <= x < H and 0 <= y < R and 0 <= z < C:
                                if box[x][y][z] == "*":
                                    cnt += 1
                ans[i][j][k] = cnt % 10

result = []
for i in range (0,H):
    for j in range (0,R):
        z = "".join(str(t) for t in ans[i][j])
        result.append(z)

for a in result:
    print(a)