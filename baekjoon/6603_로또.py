import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(arr, x):
    if len(arr) == 6:
        res.append(arr)
        return
    for i in range(x+1, len(s)):
        if not visit[i]:
            visit[i] = 1
            dfs(arr+[s[i]], i)
            visit[i] = 0

while True:
    s = list(map(int, input().split()))
    if s == [0]:
        break
    s = s[1:]
    visit = [0]*len(s)
    res = []
    dfs([], -1)
    res.sort()
    for x in res:
        print(' '.join(list(map(str, x))))
    print('')