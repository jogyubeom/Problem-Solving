res = []
for i in range(1, 6):
    agent = input()
    l = len(agent)
    for j in range(l-2):
        if agent[j:j+3] == "FBI":
            res.append(i)
            break
            
if res:
    print(*res)
else:
    print("HE GOT AWAY!")
