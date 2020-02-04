import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = [[0]*10 for _ in range(N)]
nums[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(N-1):
    for j in range(10):
        if j != 0:
            nums[i+1][j-1] += nums[i][j]
        if j != 9:
            nums[i+1][j+1] += nums[i][j]
res = 0
print(nums)
for i in range(10):
    res += nums[N-1][i]
if N > 3:
    res -= 14*(N-3)
res %= 1000000007
print(res)
 