import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(arr):
    global res
    if len(arr) == 5:
        res = 1
        return
    for i in friends[arr[-1]]:
        if not visit[i]:
            visit[i] = 1
            dfs(arr+[i])
            visit[i] = 0


n, m = map(int, input().split())
friends = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
res = 0
for i in range(n):
    visit = [0]*n
    visit[i] = 1
    dfs([i])
    if res == 1:
        break
print(res)