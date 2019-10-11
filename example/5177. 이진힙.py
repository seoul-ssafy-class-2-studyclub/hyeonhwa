def replace(node):
    if node//2 >= 1:
        if tree[node] < tree[node//2]:
            tree[node], tree[node//2] = tree[node//2], tree[node]
            replace(node//2)


def init(node):
    global idx
    if node > N:
        return
    tree[node] = nums[idx]
    idx += 1
    replace(node)
    init(node+1)


def ans(n):
    global res
    while n//2 >= 1:
        res += tree[n//2]
        n //= 2


T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    idx = 0
    tree = [0]*(N+1)
    init(1)
    res = 0
    ans(N)
    print('#{} {}'.format(t+1, res))
