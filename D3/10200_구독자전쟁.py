for t in range(int(input())):
    n, a, b = map(int, input().split())
    max_v = min(a, b)
    min_v = (a+b) - n
    if min_v < 0:
        min_v = 0
    print(f'#{t+1} {max_v} {min_v}')