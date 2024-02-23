word = input().upper()
frequency = dict()
for n in word:
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1
values = list(frequency.values())
max_value = max(values)
count = 0
for n in frequency:
    if frequency[n] == max_value:
        count += 1
        result = n
if count != 1:
    result = '?'
print(result)