for t in range(int(input())):
    n, m = map(int, input().split())
    binary = [0]*31
    x = 0
    while m:
        binary[x] = m%2
        x += 1
        m //= 2
    for i in range(n):
        if not binary[i]:
            print(f'#{t+1} OFF')
            break
    else:
        print(f'#{t+1} ON')
