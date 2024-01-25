A = int(input())
B = int(input())
C = int(input())

number = A * B * C

count_ = {}
for n in range(10):
    count_[n] = 0

num = str(number)
for n in range(len(num)):
    count_[int(num[n])] += 1

for n in range(10):
    print(count_[n])
