# LIS 알고리즘

def lis():
    res[0] = nums[0]
    loc[0] = 0
    l = 0
    for i in range(1, N):
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
    while ((end-start) > 0):
        mid = (end+start)//2
        if res[mid] < target:
            start = mid+1
        else:
            end = mid
    return end


N = int(input())
nums = list(map(int, input().split()))
res = [-1e9]*N
loc = [-1]*N
length = lis() + 1
result = [0]*length
k = length-1
while k >= 0:
    for i in range(N-1, -1, -1):
        if loc[i] == k:
            result[k] = nums[i]
            k -= 1
result = ' '.join(list(map(str, result)))
print(f'{length}\n{result}')
