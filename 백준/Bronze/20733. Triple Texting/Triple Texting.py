words = input()
temp = len(words) // 3
lst = []
for i in range(0, len(words), temp):
    lst.append(words[i:i+temp])
if lst[0] == lst[1]:
    print(lst[0])
elif lst[0] == lst[2]:
    print(lst[0])
else:
    print(lst[1])