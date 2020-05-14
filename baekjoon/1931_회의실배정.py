import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
conference = [list(map(int, input().split())) for _ in range(n)]
conference.sort(key=lambda x:(x[1], x[0]))
res = 1
s, f = conference[0]
for x, y in conference[1:]:
    if f <= x:
        s, f = x, y
        res += 1
print(res)