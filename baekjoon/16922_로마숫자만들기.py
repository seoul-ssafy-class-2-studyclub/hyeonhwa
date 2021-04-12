n = int(input())
res = set()
for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            t = n-i-j-k
            num = 1*i + 5*j + 10*k + 50*t
            res.add(num)
print(len(res))
