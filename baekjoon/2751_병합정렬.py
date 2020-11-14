def divide(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = divide(left)
    right = divide(right)
    return merge(left, right)


def merge(left, right):
    l = len(left) + len(right)
    arr = [0]*l
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[i+j] = right[j]
            j += 1
        else:
            arr[i+j] = left[i]
            i += 1
    while i < len(left):
        arr[i+j] = left[i]
        i += 1
    while j < len(right):
        arr[i+j] = right[j]
        j += 1
    return arr


n = int(input())
nums = [int(input()) for _ in range(n)]
for i in divide(nums):
    print(i)