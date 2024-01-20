# Insertion Sort
arr = [4,3,1,7,8,10,2,6,5,9]
N = len(arr)
for i in range(1, N):
    for j in range(i,0,-1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
print(arr)

# Optimized 1
arr = [4,3,1,7,8,10,2,6,5,9]
N = len(arr)
for i in range(1, N):
    for j in range(i,0,-1):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else: break
print(arr)

# Optimized 2 - (for문으로 구현하기가 왜 빡센지 모르겠네)
arr = [4,3,1,7,8,10,2,6,5,9]
N = len(arr)
for i in range(1, N):
    idx = i
    val = arr[i]
    while idx > 0 and arr[idx-1] > val:
        arr[idx] = arr[idx-1]
        idx -= 1
    arr[idx] = val
print(arr)

# 시간복잡도
# - 최선 : O(n)
# - 최악 : O(n^2) 
# 공간복잡도 : O(n), In-place sorting
# Stable Sort