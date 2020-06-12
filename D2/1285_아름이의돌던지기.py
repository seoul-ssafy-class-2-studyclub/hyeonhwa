for t in range(int(input())):
    n = int(input())
    loc = [abs(int(i)) for i in input().split()]
    loc.sort()
    print(f'#{t+1} {loc[0]} {loc.count(loc[0])}')