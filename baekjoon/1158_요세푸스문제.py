n, k = map(int, input().split())
nums = [i+1 for i in range(n)]
cnt = 1
res = [0]*n
idx1, idx2 = 0, 0
while idx1 < n:
    if cnt == k and nums[idx2]:
        res[idx1] = nums[idx2]
        nums[idx2] = 0
        idx1 += 1
        cnt = 1
    if nums[idx2] != 0:
        cnt += 1
    idx2 += 1
    if idx2 >= n:
        idx2 = 0
st = '<'
for x in range(n):
    st += str(res[x])
    if x != n-1:
        st += ', '
    else:
        st += '>'
print(st)
