N, K = map(int, input().split())

if N == K:
    print(0)
else:
    visit = [0]*10*(max(N, K))
    visit[N] = 1
    subin = [(N, 0)]
    for x, cnt in subin:
        if x + 1 < len(visit) and not visit[x+1]:
            if x + 1 == K:
                print(cnt+1)
                break
            subin.append((x+1, cnt+1))
            visit[x+1] = 1
        if x - 1 >= 0 and not visit[x-1]:
            if x - 1 == K:
                print(cnt+1)
                break
            subin.append((x-1, cnt+1))
            visit[x-1] = 1
        if 2 * x < len(visit) and not visit[2*x]:
            if 2*x == K:
                print(cnt + 1)
                break
            subin.append((x*2, cnt+1))
            visit[2*x] = 1
