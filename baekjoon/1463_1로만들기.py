n = int(input())

nums = [1e10]*(n+1)
nums[n] = 0
for i in range(n, 0, -1):
    if i%3 == 0:
        nums[i//3] = min(nums[i//3], nums[i] + 1)
    if i%2 == 0:
        nums[i//2] = min(nums[i//2], nums[i] + 1)
    nums[i-1] = min(nums[i-1], nums[i] + 1)
    if nums[1] != 1e10:
        break
print(nums[1])
