# Bubble Sort
arr = [8,4,10,3,5,1,2,7,6,9]
N = len(arr)
for i in range(N-1):
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# Optimized 1
arr = [8,4,10,3,5,1,2,7,6,9]
N = len(arr)
for i in range(N-1):
    check = False
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            check = True
    if not check: break
print(arr)

# Optimized 2 - Descending order
arr = [8,4,10,3,5,1,2,7,6,9]
N = len(arr)
end = N-1
while end:
    last_swapped = 0
    for i in range(end):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            last_swapped = i
    end = last_swapped
print(arr)

# 시간 복잡도 : O(n^2)
# 공간 복잡도 : O(n), In-placing sort
# Stable Sort