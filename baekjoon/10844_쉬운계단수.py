import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = [[0]*10 for _ in range(N)]
for i in range(N):
    for j in range(10):
        if i == 0:
            nums[i][j] = 1
        else:
            if j == 0:
                nums[i][j] = nums[i-1][j+1]
            elif j == 9:
                nums[i][j] = nums[i-1][j-1]
            else:
                nums[i][j] = nums[i-1][j-1] + nums[i-1][j+1]
res = 0
print(nums)
for i in range(1, 10):
    res += nums[N-1][i]
res %= 1000000000
print(res)
