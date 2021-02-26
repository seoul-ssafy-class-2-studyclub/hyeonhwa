n, s = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0, 0
total = 0
res = 1e10
while True:
    if total >= s:
        res = min(res, end-start)
        total -= nums[start]
        start += 1
    elif end == n:
        break
    else:
        total += nums[end]
        end += 1
if res == 1e10:
    res = 0
print(res)
