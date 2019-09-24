def backtrack(idx, x, cnt):
    global res
    if cnt >= res:
        return
    if idx + x >= info[0]:
        if res > cnt:
            res = cnt
        return 
    for i in info[idx+1:idx+x+1]:
        idx += 1
        x = i
        backtrack(idx, x, cnt+1)


T = int(input())
for t in range(T):
    info = list(map(int, input().split()))
    res = 10000000
    backtrack(1, info[1], 0)
    print(f'#{t+1} {res}')
