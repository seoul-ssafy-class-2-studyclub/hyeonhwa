n = int(input())
l = list(map(int, input().split()))
l.sort()
s, e = 0, n-1
res = l[s] + l[e]
idx = [s, e]
while s < e:
    tmp = l[s] + l[e]
    if abs(tmp) < abs(res):
        res = tmp
        idx = [s, e]
        if res == 0:
            break
    if tmp < 0:
        s += 1
    else:
        e -= 1
print(l[idx[0]], l[idx[1]])
