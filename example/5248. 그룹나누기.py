def dfs(x):
    queue = [x]
    while queue:
        x = queue.pop()
        if not visited[x]:
            visited[x] = True
            queue.extend(wanted[x])


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    wanted = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    for i in range(0, len(nums), 2):
        wanted[nums[i]].append(nums[i+1])
        wanted[nums[i+1]].append(nums[i])
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == False:
            dfs(i)
            cnt += 1
    print('#{} {}'.format(t+1, cnt))