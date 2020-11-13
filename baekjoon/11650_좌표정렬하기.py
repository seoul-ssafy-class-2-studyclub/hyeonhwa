n = int(input())
loc = [list(map(int, input().split())) for _ in range(n)]
for x, y in sorted(loc, key=lambda x:(x[0], x[1])):
    print(x, y)
