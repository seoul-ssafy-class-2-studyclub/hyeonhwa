'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    left, right = [], []
    equal = []
    pivot = arr[len(arr)//2]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    return quick_sort(left) + equal + quick_sort(right)
'''

# <in-place : 메모리 효율 >
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)
    
    def partition(low, high):
        pivot = arr[(low+high)//2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[high], arr[low] = arr[low], arr[high]
                low += 1
                high -= 1
        return low
    return sort(0, len(arr)-1)

T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums)
    print(f'#{t+1} {nums[N//2]}')