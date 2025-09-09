arr = [int(input()) for i in range(10)]

for i in range(10):
    arr[i] = arr[i] % 42

print(len(list(set(arr))))