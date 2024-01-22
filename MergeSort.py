# Merge Sort
arr = [8,4,3,1,6,7,2,10,9,5]
N = len(arr)

def MergeSort(arr, lo, hi):
    if hi - lo < 1: return
    mid = (lo + hi) // 2
    MergeSort(arr, lo, mid)
    MergeSort(arr, mid+1, hi)
    Merge(arr, lo, mid, hi)

def Merge(arr, lo, mid, hi):
    temp = []
    i, j = lo, mid+1

    while i <= mid and j <= hi:
        if arr[i] > arr[j]:
            temp.append(arr[j])
            j += 1
        else:
            temp.append(arr[i])
            i += 1

    while i <= mid: 
        temp.append(arr[i])
        i += 1

    while j <= hi: 
        temp.append(arr[j])
        j += 1

    arr[lo:hi + 1] = temp

MergeSort(arr, 0, N-1)
print(arr)

# 시간복잡도 : O(nlogn)
# 공간복잡도 : 코드 짜는 거에 따라 좀 다름
# Stable Sort