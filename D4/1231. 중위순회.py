import sys
sys.stdin = open('tree.txt', 'r')

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# def treeadd(root, node):
#     if root.data > node.data:
#         if root.left == None:
#             root.left = node
#         else:
#             treeadd(root.left, node)
#     else:
#         if root.right == None:
#             root.right = node
#         else:
#             treeadd(root.right, node)


# def inorder(node):
#     global res
#     if not node:
#         return
#     inorder(node.left)
#     res += [node.data]
#     inorder(node.right)

def inorder(x):
    global res
    if x <= N:
        inorder(x * 2)
        res += Table[x]
        inorder(x * 2+1)
 
 
for t in range(10):
    N = int(input())
    Table = [0] * (N+1)
    for i in range(N):
        Data = input().split()
        Table[i+1] = Data[1]
    res = ''
    inorder(1)
    print('#{} {}'.format(t+1, res))
