# Binary Search
arr = [1, 2, 3, 4, 5, 10, 12, 13, 15, 21, 30, 42, 78, 230, 230, 230, 230, 230, 230, 230, 843, 845, 42237, 48562]
print(arr)
lo, hi = -1, len(arr)
val = 500
while lo+1 < hi:
    mid = (lo+hi)//2
    if arr[mid] < val:
        lo = mid
    else:
        hi = mid
print(hi)

# Lower Bound
def lower_bound(arr, val):
    arr = sorted(arr)
    lo, hi = -1, len(arr)
    while lo+1 < hi:
        mid = (lo+hi)//2
        if arr[mid] < val:
            lo = mid
        else:
            hi = mid
    return lo+1

def upper_bound(arr, val):
    arr = sorted(arr)
    lo, hi = -1, len(arr)
    while lo+1 < hi:
        mid = (lo+hi)//2
        if arr[mid] <= val:
            lo = mid
        else:
            hi = mid
    return lo+1

print(lower_bound(arr, 230))
print(upper_bound(arr, 230))
print(upper_bound(arr, 230) - lower_bound(arr, 230))