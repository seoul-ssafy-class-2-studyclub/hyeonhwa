import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(arr):
    if len(arr) == m:
        print(' '.join(list(map(str, arr))))
        return
    for i in range(n):
        if visit[i+1]:
            continue
        visit[i+1] = 1
        solve(arr+[nums[i]])
        visit[i+1] = 0

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visit = [0]*(n+1)
solve([])