from pprint import pprint
'''
1
5
0 1 1 0 0
0 0 1 0 3
0 1 0 1 0
0 0 0 0 0
1 0 5 0 0
'''

def gostairs(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split()))for _ in range(N)]
