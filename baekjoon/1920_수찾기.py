def find(x):
    s, e = 0, len(nums)
    while s < e:
        mid = (s + e)//2
        if nums[mid] == x:
            return 1
        elif nums[mid] < x:
            s = mid + 1
        else:
            e = mid
    return 0


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
for num in map(int, input().split()):
    print(find(num))
