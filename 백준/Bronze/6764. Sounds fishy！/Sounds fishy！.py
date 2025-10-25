arr = []
for _ in range(4):
    arr.append(int(input()))

if arr[0] == arr[1] == arr[2] == arr[3]:
    print("Fish At Constant Depth")
elif len(arr) == len(set(arr)) and arr == sorted(arr):
    print("Fish Rising")
elif len(arr) == len(set(arr)) and arr == sorted(arr, reverse=True):
    print("Fish Diving")
else:
    print("No Fish")