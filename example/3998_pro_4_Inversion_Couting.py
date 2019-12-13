# Merge Sort
def divide(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    leftlist = arr[:mid]
    rightlist = arr[mid:]
    leftlist = divide(leftlist)
    rightlist = divide(rightlist)   
    return merge(leftlist, rightlist)


def merge(left, right):
    global cnt
    l = len(left) + len(right)
    arr = [0 for _ in range(l)]
    j, k = 0, 0
    while j < len(right) and k < len(left):
        if left[k] > right[j]:
            cnt += len(left) - k
            arr[j+k] = right[j]
            j += 1
        elif left[k] <= right[j]:
            arr[j+k] = left[k]  
            k += 1
    while j < len(right):
        arr[j+k] = right[j]
        j += 1
    while k < len(left):
        arr[k+j] = left[k]
        k += 1
    return arr


T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    divide(nums)
    print(f'#{t+1} {cnt}')
