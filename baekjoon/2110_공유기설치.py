n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()
s = 0
e = house[-1]
res = 0
while s <= e:
    mid = (s+e)//2
    x = house[0]
    cnt = 1
    for i in range(1, n):
        if house[i] - x >= mid:
            cnt += 1
            x = house[i]
    if cnt >= c:
        s = mid+1
        res = mid
    else:
        e = mid-1
print(res)
