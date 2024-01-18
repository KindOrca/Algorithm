# Insertion Sort
arr = [4,3,1,7,8,10,2,6,5,9]
N = len(arr)
for i in range(1,N):
    for j in range(i,0,-1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
print(arr)

# Optimized 1


# Optimized 2

