def makeTree1(left, right, node):
    if left == right:
        tree1[node] = nums[left]
        return tree1[node]
    mid = (left+right) // 2
    tree1[node] = max(makeTree1(left, mid, node*2), makeTree1(mid+1, right, node*2+1))
    return tree1[node]


def makeTree2(left, right, node):
    if left == right:
        tree2[node] = nums[left]
        return tree2[node]
    mid = (left+right) // 2
    tree2[node] = min(makeTree2(left, mid, node*2), makeTree2(mid+1, right, node*2+1))
    return tree2[node]


def findminvalue(start, end, n, left, right):
    if right < start or left > end:
        return 1000000001
    if start >= left and start <= right and end >= left and end <= right:
        return tree2[n]
    return min(findminvalue(start, (start+end)//2, n*2, left, right), findminvalue((start+end)//2+1, end, n*2+1, left, right))


def findmaxvalue(start, end, n, left, right):
    if right < start or left > end:
        return 0
    if start >= left and start <= right and end >= left and end <= right:
        return tree1[n]
    return max(findmaxvalue(start, (start+end)//2, n*2, left, right), findmaxvalue((start+end)//2+1, end, n*2+1, left, right))


N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
tree1 = [0]*(4*N)
tree2 = [0]*(4*N)
makeTree1(0, N-1, 1)
makeTree2(0, N-1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    res1 = findminvalue(0, N-1, 1, a-1, b-1)
    res2 = findmaxvalue(0, N-1, 1, a-1, b-1)
    print(f'{res1} {res2}')
