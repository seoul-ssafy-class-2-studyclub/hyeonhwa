def quick(arr):
    if len(arr) <= 1:
        return arr
    left, right, mid = [], [], []
    pivot = arr[len(arr)//2]
    for x in arr:
        if x > pivot:
            right.append(x)
        elif x < pivot:
            left.append(x)
        else:
            mid.append(x)
    return quick(right) + mid + quick(left)


n = [int(i) for i in input()]
res = quick(n)
print(''.join(list(map(str, res))))