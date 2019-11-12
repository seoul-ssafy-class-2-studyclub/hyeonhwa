def calculator(a, b, n):
    if n == '+':
        return a+b
    if n == '-':
        return a-b
    if n == '*':
        return a*b
    if n == '/':
        if a < 0:
            return -((-a)//b)
        else:
            return a//b


def comb(arr, n, idx):
    global maxnum
    global minnum
    if len(arr) == len(cal):
        if n > maxnum:
            maxnum = n
        if n < minnum:
            minnum = n
        return
    if minnum < n < maxnum:
        return
    for i in range(len(cal)):
        if visited[i] == False:
            if nums[idx] == 0:
                continue
            visited[i] = True
            comb(arr+[cal[i]], calculator(n, nums[idx], cal[i]), idx+1)
            visited[i] = False


T = int(input())
for t in range(T):
    N = int(input())
    cals = list(map(int, input().split()))
    cal = ['+']*cals[0] + ['-'] * cals[1] + ['*']*cals[2] +  ['/']*cals[3]
    nums = list(map(int, input().split()))
    visited = [False]*len(cal)
    maxnum, minnum = 0, 100000000
    comb([], nums[0], 1)
    print(f'#{t+1} {maxnum-minnum}')
