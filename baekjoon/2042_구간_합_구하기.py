def bit_update(idx, value):
    while idx <= N:
        bit[idx] += value
        idx += (idx & (-idx))


def bit_sum(idx):
    res = 0
    while idx > 0:
        res += bit[idx]
        idx -= (idx & (-idx))
    return res


N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
bit = [0]*(4*N)
for i in range(1, N+1):
    bit_update(i, nums[i-1])
result = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        val = c - nums[b-1]
        nums[b-1] = c
        bit_update(b, val)
    else:
        result.append(bit_sum(c)-bit_sum(b-1))
print('\n'.join(list(map(str, result))))
