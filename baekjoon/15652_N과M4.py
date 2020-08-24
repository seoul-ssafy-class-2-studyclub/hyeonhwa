import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(arr):
    if len(arr) == m:
        print(' '.join(list(map(str, arr))))
        return
    for i in range(n):
        if arr and arr[-1] > i+1:
            continue
        solve(arr+[i+1])

n, m = map(int, input().split())
solve([])