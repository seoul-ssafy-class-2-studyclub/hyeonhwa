def diff(idx, s):
    global res
    if idx < N and s < B:
        temp = s + height[idx]
        if temp < res:
            diff(idx+1, temp)
            if temp >= B:
                res = temp
        diff(idx+1, s)


T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    res = 1000000
    diff(0, 0)
    print(f'#{t+1} {res-B}')