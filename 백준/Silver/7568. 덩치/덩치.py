
def check(a, b):
    if a[0] > b[0] and a[1] > b[1]:
        return 1
    else:
        return 0

people = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    people.append((a, b))
for person in people:
    count = 0
    for i in range(len(people)):
        count += check(people[i], person)
    print(count + 1, end=' ')