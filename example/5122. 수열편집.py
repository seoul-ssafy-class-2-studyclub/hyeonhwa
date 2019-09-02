T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    nums = list(input().split())
    for _ in range(M):
        change = list(input().split())
        if change[0] == 'I':
            nums.insert(int(change[1]), change[2])
        elif change[0] == 'D':
            del nums[int(change[1])]
        elif change[0] == 'C':
            nums[int(change[1])] = change[2]
    if L >= len(nums):
        print('#{} -1'.format(t+1))
    else:
        print('#{} {}'.format(t+1, nums[L]))
