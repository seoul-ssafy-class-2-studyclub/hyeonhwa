def perm(arr):
    if len(arr) == l:
        res.append(arr)
        return
    for i in range(l):
        if not visit[i]:
            visit[i] = True
            perm(arr+[op[i]])
            visit[i] = False


def cals(arr1, arr2):
    stack = []
    for i in range(N):
        if not stack:
            stack.append(arr1[i])
            continue
        x = arr2.pop(0)
        if x == '+':
            stack[0] += arr1[i]
        elif x == '-':
            stack[0] -= arr1[i]
        elif x == '*':
            stack[0] *= arr1[i]
        elif x == '/':
            if stack[0] < 0:
                stack[0] = -stack[0]
                stack[0] //= arr1[i]
                stack[0] = -stack[0]
            else:
                stack[0] //= arr1[i]
    return stack[0]


N = int(input())
nums = list(map(int, input().split()))
opnum = list(map(int, input().split()))
op = ['+']*opnum[0] + ['-']*opnum[1] + ['*']*opnum[2] + ['/']*opnum[3]
l = len(op)
visit = [False]*l
res = []
perm([])
maxn = -10000000000
minn = 10000000000
for i in res:
    num = cals(nums, i)
    if num > maxn:
        maxn = num
    if num < minn:
        minn = num
print(maxn)
print(minn)
