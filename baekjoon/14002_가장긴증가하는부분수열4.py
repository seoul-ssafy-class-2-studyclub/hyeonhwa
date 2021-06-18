def lis(res, loc):
    res[0] = nums[0]
    loc[0] = 0
    l = 0
    for i in range(1, n):
        if res[l] < nums[i]:
            res[l+1] = nums[i]
            loc[i] = l+1
            l += 1
        else:
            idx = findidx(0, l, nums[i])
            res[idx] = nums[i]
            loc[i] = idx
    return l

def findidx(start, end, target):
    while end > start:
        mid = (end+start)//2
        if res[mid] < target:
            start = mid+1
        else:
            end = mid
    return end

n = int(input())
nums = list(map(int, input().split()))
res = [0]*n
loc = [-1]*n
length = lis(res, loc) + 1
k = length - 1
result = [0]*length
while k >= 0:
    for i in range(n-1, -1, -1):
        if loc[i] == k:
            result[k] = nums[i]
            k -= 1
result = ' '.join(map(str, result))
print(f'{length}\n{result}')
