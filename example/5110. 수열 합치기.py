T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(M-1):
        x = list(map(int, input().split()))
        k = x[0]
        l = len(nums)
        flag = 0
        for j in range(len(nums)):
            if nums[j] > k:
                flag = 1
                nums[j:0] = x  # nums = nums[:j] + x + nums[j:]
                break
        if flag == 0:
            nums += x      
    print('#{} {}'.format(t+1, ' '.join(map(str, nums[-1:-11:-1]))))
