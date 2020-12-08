prime = [1]*(10**7+1)
prime[0], prime[1] = 0, 0
x = 2
while x*x < len(prime):
    if prime[x]:
        for j in range(x*x, len(prime), x):
            if prime[j]:
                prime[j] = 0
    x += 1

for t in range(int(input())):
    n = int(input())
    nums = {}
    while n > 1:
        for i in range(2, n+1):
            if prime[i] and n%i == 0:
                if nums.get(i):
                    nums[i] += 1
                else:
                    nums[i] = 1
                n //= i
                break
    res = 1
    for key, value in nums.items():
        if value%2:
            res *= key
    print(f'#{t+1} {res}')
