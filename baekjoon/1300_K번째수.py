n = int(input())
k = int(input())
s, e = 1, k
while s <= e:
    # m 이 B[k] 인지 판단
    m = (s+e)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, m//i)
    if cnt < k:
        s = m + 1
    else:
        e = m - 1
print(s)