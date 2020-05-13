import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
res = []
cnt = []
for i in range(1, n+1):
    num = nums[i]
    if i == num:
        cnt.append(num)
        continue
    queue = [num]
    visit = [0]*(n+1)
    visit[num] = 1
    idx = [i]
    for x in queue:
        if not visit[nums[x]]:
            queue.append(nums[x])
            idx.append(x)
            visit[nums[x]] = 1
    if sorted(queue) == sorted(idx):
        res.extend(queue)
res = list(set(res))
res = [len(res+cnt)] + sorted(res + cnt)
print('\n'.join(list(map(str, res))))