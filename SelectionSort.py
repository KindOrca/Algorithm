# Selection Sort
arr = [7,6,4,3,1,2,10,9,8,5]
N = len(arr)
for i in range(N):
    idx = i
    for j in range(i+1, N):
        if arr[idx] > arr[j]:
            idx = j
    arr[i], arr[idx] = arr[idx], arr[i]
print(arr)