import sys
input = lambda: sys.stdin.readline().rstrip()

def cal(arr):
    s = 0
    for i in range(n-1):
        s += abs(arr[i]-arr[i+1])
    return s


def func(arr):
    global res
    if len(arr) == n:
        res = max(res, cal(arr))
    for i in range(n):
        if visit[i]:
            continue
        visit[i] = 1
        func(arr + [nums[i]])
        visit[i] = 0


n = int(input())
nums = list(map(int, input().split()))
res = 0
visit = [0]*n
func([])
print(res)