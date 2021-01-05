for t in range(int(input())):
    nums = [int(i) for i in input().split()]
    nums.sort()
    total = 0
    for i in range(1, len(nums)-1):
        total += nums[i]
    total = round(total/8)
    print(f'#{t+1} {total}')
