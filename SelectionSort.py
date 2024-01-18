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


# 백준 23883번
# 이거 왜 안됨? 시간초과도 아니고 왜 틀렸습니다로 나오는지 생각
import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
PQ = PriorityQueue()
dic = dict()
cnt = 0
for i in range(N-1):
    dic[A[i]] = i
    PQ.put(-A[i])
dic[A[N-1]] = N-1

for i in range(N-1,0,-1):
    idx = dic[-PQ.get()]
    if idx == i: continue
    A[idx], A[i] = A[i], A[idx]
    cnt += 1
    if cnt == K:
        print(A[idx], A[i])
        break
    dic[A[idx]] = idx
    PQ.put(-A[idx])
else:
    print(-1)