arr = [55, 7, 78, 12, 42]
n = len(arr)
for i in range(n - 1):
    if arr[i] > arr[i+1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(arr)



for i in range(n - 2):
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(arr)


for j in range(n - 1, 0, -1):
    for i in range(j):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(arr)


MIN = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arr[MIN]:
        MIN = arr[i]

print(MIN)


MIN = 0
for i in range(1, len(arr)):
    if arr[i] < arr[MIN]:
        MIN = i
arr[0], arr[MIN] = arr[MIN], arr[0]
print(arr)



arr = [55, 7, 78, 12, 42]
for j in range(len(arr) - 1):
    MIN = j
    for i in range(j + 1, len(arr)):
        if arr[i] < arr[MIN]:
            MIN = i
    arr[j], arr[MIN] = arr[MIN], arr[j]
print(arr)