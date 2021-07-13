n = int(input())
l = list(map(int, input().split()))
l.sort()
total = int(input())
s, e = 0, l[n-1]
while s <= e:
    mid = (s+e)//2
    amount = 0
    for x in l:
        if x <= mid:
            amount += x
        else:
            amount += mid
    if total < amount:
        e = mid-1
    else:
        s = mid+1
print(e)