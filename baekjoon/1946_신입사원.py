import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    nums.sort(key=lambda x:(x[0], x[1]))
    xx, yy = n+1, n+1
    res = 0
    for x, y in nums:
        if x <= xx or y <= yy:
            res += 1
            xx, yy = x, y
    print(res)