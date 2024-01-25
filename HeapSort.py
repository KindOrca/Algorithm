# Heap Sort
A = [4,7,3,1,6,10,2,9,8,5]
N = len(A)

def build_min_heap(A, n):
    for i in range(n//2,-1,-1):
        heapify(A, i , n)

def heapify(A, k, n):
    lo, hi = 2*k, 2*k+1
    if hi <= n:
        if A[lo] < A[hi]:
            idx = lo
        else:
            idx = hi
    elif lo <= n:
        idx = lo
    else:
        return
    
    if A[idx] < A[k]:
        A[idx], A[k] = A[k], A[idx]
        heapify(A, idx, n)

build_min_heap(A, N-1)
for i in range(N-1, 0, -1):
    A[0], A[i] = A[i], A[0]
    heapify(A, 0, i-1)

print(A)

# 시간복잡도 : O(nlogn)
# 완전 이진 트리를 기본으로 하는 힙(Heap) 자료구조를 기반으로한 정렬 방식