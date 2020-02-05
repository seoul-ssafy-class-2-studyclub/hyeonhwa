import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
'''
[N][10][현재 상태] : 10 = 끝나는 수
현재 상태
0 : 2번 감소
1 : 1번 감소
2 : x
3 : 1번 증가
4 : 2번 증가
'''
nums = [[[0]*5 for _ in range(10)] for _ in range(N+1)]
for i in range(10):
    nums[0][i][2] = 1
for i in range(10):
    if i == 0:
        nums[1][i][1] = nums[0][i-1][2]
    elif i == 9:
        nums[1][i][3] = nums[0][i-1][2]
    else:
        nums[1][i][3] = nums[0][i-1][2]
        nums[1][i][1] = nums[0][i+1][2]
for i in range(2, N):
    for j in range(10):
        if j == 0:
            nums[i][j][0] = nums[i-1][j+1][1]
            nums[i][j][1] = nums[i-1][j+1][3]
        elif j == 9:
            nums[i][j][3] = nums[i-1][j-1][1]
            nums[i][j][4] = nums[i-1][j-1][3]
        else:
            nums[i][j][0] = nums[i-1][j+1][1]
            nums[i][j][1] = nums[i-1][j+1][3] + nums[i-1][j+1][4]
            nums[i][j][3] = nums[i-1][j-1][1] + nums[i-1][j-1][0]
            nums[i][j][4] = nums[i-1][j-1][3]
res = 0
for i in range(10):
    res += sum(nums[N-1][i])
res %= 1000000007
print(res)
 