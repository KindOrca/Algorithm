# Quick Sort
A = [4,7,3,1,6,10,2,9,8,5]
N = len(A)

def QuickSort(arr, lo, hi):
    if lo >= hi: return
    pivot = partition(arr, lo, hi)
    QuickSort(arr, lo, pivot-1)
    QuickSort(arr, pivot+1, hi)

def partition(arr, lo, hi):
    pivot = arr[lo]
    i, j = lo, hi
    while i < j:
        while pivot < arr[j]: j -= 1
        while i < j and pivot >= arr[i]: i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[i] = arr[i], arr[lo]
    return i

QuickSort(A, 0, N-1)
print(A)

# 시간복잡도
# - 최선 : O(nlogn)
# - 최악 : O(n^2)
# 공간복잡도 : O(n)
# In-place Sorting
# Unstable Sort