import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])
res=float('inf')
i,j=0,0
while i<n and j<n:
    if nums[j] - nums[i] >= m:
        res=min(res, nums[j]- nums[i])
        i += 1
    else: j += 1
print(res)