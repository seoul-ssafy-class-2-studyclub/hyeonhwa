from collections import deque

def queue(x):
    if x[:4] == 'push':
        q.append(x[5:])
    elif x == 'pop':
        if not q:
            res.append('-1')
        else:
            res.append(q.popleft())
    elif x == 'size':
        res.append(str(len(q)))
    elif x == 'empty':
        if not q:
            res.append('1')
        else:
            res.append('0')
    elif x == 'front':
        if not q:
            res.append('-1')
        else:
            res.append(q[0])
    elif x == 'back':
        if not q:
            res.append('-1')
        else:
            res.append(q[-1])


N = int(input())
q = deque()
res = []
for _ in range(N):
    x = input()
    queue(x)
print('\n'.join(res))
