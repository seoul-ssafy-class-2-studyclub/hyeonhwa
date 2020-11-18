class Node:
    def __init__(self, item, l, r):
        self.item = item
        self.l = l
        self.r = r

# 전위순회 root -> left -> right
def preorder(node):
    pre.append(node.item)
    if node.l != '.':
        preorder(tree[node.l])
    if node.r != '.':
        preorder(tree[node.r])

# 중위순회 left -> root -> right
def inorder(node):
    if node.l != '.':
        inorder(tree[node.l])
    ino.append(node.item)
    if node.r != '.':
        inorder(tree[node.r])

# 후위순회 left -> right -> root
def postorder(node):
    if node.l != '.':
        postorder(tree[node.l])
    if node.r != '.':
        postorder(tree[node.r])
    post.append(node.item)

n = int(input())
tree = {}
for _ in range(n):
    a, b, c = input().split()
    tree[a] = Node(a, b, c)
pre = []
ino = []
post = []
preorder(tree['A'])
inorder(tree['A'])
postorder(tree['A'])
print(''.join(pre))
print(''.join(ino))
print(''.join(post))
