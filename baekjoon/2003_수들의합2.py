n, m = map(int, input().split())
nums = list(map(int, input().split()))
res = 0
total = 0
s = 0
for num in nums:
    total += num
    if total >= m:
        while total >= m:
            if total == m:
                res += 1
            total -= nums[s]
            s += 1
print(res)
