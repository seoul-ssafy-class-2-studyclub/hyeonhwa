for t in range(10):
    L = int(input())
    h = input().split(' ')
    n = 2
    cnt = 0
    while n < len(h)-1:
        if int(h[n]) <= 255:
            if int(h[n]) > int(h[n-1]) and int(h[n]) > int(h[n-2]) and int(h[n]) > int(h[n+1]) and int(h[n]) > int(h[n+2]):
                cnt += int(h[n]) - max(int(h[n-1]), int(h[n-2]), int(h[n+1]), int(h[n+2]))
        n += 1
        print(f'#{t+1} {cnt}')
