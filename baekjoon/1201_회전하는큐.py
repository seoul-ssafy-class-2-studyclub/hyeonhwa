def cals(x, arr):
    if x == 1:
        arr.append(arr.pop(0))
    else:
        arr.insert(0, arr.pop())
    return arr


n, m = map(int, input().split())
locs = list(int(i) for i in input().split())
cnt = 0
nums = [i for i in range(1, n+1)]
while locs:
    if nums[0] == locs[0]:
        nums.pop(0)
        locs.pop(0)
    else:
        if nums.index(locs[0]) <= len(nums) // 2:
            while nums[0] != locs[0]:
                nums = cals(1, nums)
                cnt += 1
        else:
            while nums[0] != locs[0]:
                nums = cals(2, nums)
                cnt += 1
print(cnt)