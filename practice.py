# practice - Descending Order
arr = [5,4,8,7,3,1,6,10,2,9]

# Bubble Sort
# 바로 인접한 두수를 비교하여 기준에 맞게 교체하면서 정렬
N = len(arr)
for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)

# Optimized
arr = [5,4,8,7,3,1,6,10,2,9]
N = len(arr)
for i in range(N-1,0,-1):
    check = True
    for j in range(i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            check = False
    if check: break
print(arr)

arr = [5,4,8,7,3,1,6,10,2,9]
N = len(arr)
end = N-1
while end:
    last_idx = 0
    for i in range(end):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            last_idx = i
    end = last_idx
print(arr)

print("-----------------------------")

# Selection Sort
# 위치를 지정한 후 그 조건에 맞는 수를 찾아서 배치
arr = [5,4,8,7,3,1,6,10,2,9]
N = len(arr)
for i in range(N-1):
    idx = i
    for j in range(i+1, N):
        if arr[j] > arr[idx]:
            idx = j
    arr[idx], arr[i] = arr[i], arr[idx]
print(arr)

print('--------------------------')

# Insertion Sort
# 2번째 원소부터 시작하여 그 앞의 원소들과 비교하여 삽입할 위치를 지정한후 원소들을 뒤로 옮기고 지정
# 2번째 원소부터 시작하여 그 앞의 원소들과 비교한여 위치를 지정한 다음 원소들을 뒤로 옮기고 지정
arr = [5,4,8,7,3,1,6,10,2,9]
N = len(arr)
for i in range(1, N):
    for j in range(i,0,-1):
        if arr[j-1] < arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
        else: break
print(arr)

# Optimized
arr = [5,4,8,7,3,1,6,10,2,9]
N = len(arr)
for i in range(1, N):
    idx = i
    val = arr[i]
    while idx > 0 and arr[idx-1] > val:
        arr[idx] = arr[idx-1]
        idx -= 1
    arr[idx] = val
print(arr)

# Quick Sort
# 분할 정복을 이용하여 배열, 피봇을 정한 후 피봇 앞에는 피봇 보다 작은 값이, 피봇 뒤에는 피봇보다 큰 값이 오도록 한다.
arr = [5,4,8,7,3,1,6,10,2,9]
N = len(arr)

def QuickSort(arr, lo, hi):
    if lo >= hi: return
    pivot = partition(arr, lo, hi)
    QuickSort(arr, lo, pivot-1)
    QuickSort(arr, pivot+1, hi)

def partition(arr, lo, hi):
    pivot = arr[lo]
    i, j = lo, hi
    while i < j:
        while arr[j] < pivot: j -= 1
        while i < j and arr[i] >= pivot: i +=1
        arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[i] = arr[i], arr[lo]
    return i

QuickSort(arr, 0, N-1)
print(arr)

print("-------------------------------")

# Merge Sort
arr = [5,4,8,7,3,1,6,10,2,9]
N = len(arr)

def MergeSort(arr, lo, hi):
    if lo >= hi: return
    mid = (lo + hi) // 2
    MergeSort(arr, lo, mid)
    MergeSort(arr, mid+1, hi)
    Merge(arr, lo, mid, hi)

def Merge(arr, lo, mid, hi):
    temp = []
    i, j = lo, mid+1
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    while  i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= hi:
        temp.append(arr[j])
        j += 1
    
    arr[lo:hi+1] = temp

MergeSort(arr, 0, N-1)
print(arr)