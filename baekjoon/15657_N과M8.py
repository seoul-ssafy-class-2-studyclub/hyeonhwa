import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(arr):
    if len(arr) == m:
        print(' '.join(list(map(str, arr))))
        return
    for i in range(n):
        if arr and arr[-1] > nums[i]:
            continue
        solve(arr+[nums[i]])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
solve([])