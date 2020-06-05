def divide(n, m):
    center = (n+y, m+i)
    k = 0
    arr = [(n+y, m+i)]
    nums = [0, 0, 0, 0, 0]
    d1, d2 = 0, 0
    while True:
        dx, dy = idx[k]
        a = n+dx
        b = m+dy
        if 0 <= a < x and 0 <= b < x:
            if (dx, dy) == idx[0]:
                d1 += 1
            elif (dx, dy) == idx[1]:
                d2 += 1
            n, m = a, b
            arr.append((a+y, b+i))
            if (a+y, b+i) == center:
                arr.pop()
                break
        elif b == -1:
            k = 1
        elif a == x:
            k = 2
        elif b == x:
            k = 3
    ddy = 1
    for a, b in arr[1:(d1+d2)]:
        d = b+ddy
        while (a, d) not in arr:
            if 0 < d < N:
                arr.append((a, d))
                d += ddy
            if d == N:
                break
    for a, b in arr:
        nums[4] += city[a][b]
    for e in range(N):
        for f in range(N):
            if 0 <= e < center[0] + d1 and 0 <= f <= center[1] and (e, f) not in arr:
                nums[0] += city[e][f]
            elif 0 <= e <= center[0] + d2 and center[1] < f < N and (e, f) not in arr:
                if 0 <= e < N and 0 <= f-1 < N and (e, f+1) in arr:
                    nums[2] += city[e][f]
                    continue
                nums[1] += city[e][f]               
            elif center[0] + d1 <= e < N and 0 <= f < center[1] - d1 + d2 and (e, f) not in arr:
                if 0 <= e < N and 0 <= f-1 < N and (e, f-1) in arr:
                    nums[1] += 1
                    continue
                nums[2] += city[e][f]
            elif center[0] + d2 < e < N and center[1] - d1 + d2 <= f < N and (e, f) not in arr:
                nums[3] += city[e][f]
    return nums


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
idx = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
res = 987654321
for x in range(N-1, 2, -1):
    for y in range(1, N-x):
        for i in range(1, N-x):
            for l in range(1, x-1):
                nums = divide(0, l)
                res = min(res, (max(nums)-min(nums)))
print(res)
