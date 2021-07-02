k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
lines.sort()
s = 1
e = lines[-1]
while s <= e:
    mid = (s+e)//2
    cnt = 0
    for line in lines:
        cnt += line//mid
    if cnt >= n:
        s = mid+1
    else:
        e = mid-1
print(e)
