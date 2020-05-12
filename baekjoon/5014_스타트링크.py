import sys
input = lambda: sys.stdin.readline().rstrip()

f, s, g, u, d = map(int, input().split())
res = -1
if s == g: res = 0
else:
    building = [0]*(f+1)
    queue = [(s, 0)]
    building[s] = 1
    for x, cnt in queue:
        if 0 < x+u <= f and not building[x+u]:
            if x+u == g:
                res = cnt+1
                break
            queue.append((x+u, cnt+1))
            building[x+u] = 1
        if 0 < x-d <= f and not building[x-d]:
            if x-d == g:
                res = cnt+1
                break
            queue.append((x-d, cnt+1))
            building[x-d] = 1
if res == -1: res='use the stairs'
print(res)