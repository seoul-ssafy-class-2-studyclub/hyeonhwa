def quick(arr):
    if len(arr) <= 1:
        return arr
    left = []
    right = []
    mid = []
    pivot = arr[len(arr)//2]
    for i in arr:
        if i < pivot:
            left.append(i) 
        elif i > pivot:
            right.append(i)
        else:
            mid.append(i)
    return quick(left) + mid + quick(right)

n = int(input())
nums = [int(input()) for _ in range(n)]
# for i in sorted(nums):
#     print(i)
for i in quick(nums):
    print(i)