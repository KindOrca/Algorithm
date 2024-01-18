# Selection Sort
arr = [7,6,4,3,1,2,10,9,8,5]
N = len(arr)
for i in range(N-1):
    idx = i
    for j in range(i+1, N):
        if arr[idx] > arr[j]:
            idx = j
    arr[i], arr[idx] = arr[idx], arr[i]
print(arr)

# 시간 복잡도 : O(n^2)
# 공간 복잡도 : O(n), In-placing Sort
# Non-stable sort