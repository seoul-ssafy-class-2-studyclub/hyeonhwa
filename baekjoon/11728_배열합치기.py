n, m = map(int, input().split())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
res = [0]*(n+m)
i, j = 0, 0
while i < n and j < m:
    if num1[i] < num2[j]:
        res[i+j] = num1[i]
        i += 1
    else:
        res[i+j] = num2[j]
        j += 1
for x in range(i, n):
    res[x+j] = num1[x]
for y in range(j, m):
    res[i+y] = num2[y]
print(' '.join(list(map(str, res))))