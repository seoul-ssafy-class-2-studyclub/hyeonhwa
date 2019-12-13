def bit_update(idx, dif):
    while (idx <= N):
        binary_indexed_tree[idx] += dif
        idx = idx + (idx & (-idx))


def bit_sum(idx):
    res = 0
    while idx > 0:
        res = res + binary_indexed_tree[idx]
        idx = idx -  (idx & (-idx))
    return res


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    binary_indexed_tree = [0]*(N*2)
    for i in range(1, N+1):
        bit_update(i, nums[i-1])
    res = []
    for _ in range(M):
        c, x, y = map(int, input().split())
        if c == 1:
            bit_update(x, y)
        else:
            res.append(bit_sum(y) - bit_sum(x-1))
    res = ' '.join(list(map(str, res)))
    print(f'#{t+1} {res}')