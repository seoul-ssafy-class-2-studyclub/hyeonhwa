prime = [1]*1001
prime[0], prime[1] = 0, 0
i = 2
while i*i <= 1000:
    if prime[i]:
        for j in range(i*i, 1001, i):
            if prime[j]:
                prime[j] = 0
    i += 1

n = int(input())
nums = list(map(int, input().split()))
res = 0
for num in nums:
    if prime[num]:
        res += 1
print(res)
