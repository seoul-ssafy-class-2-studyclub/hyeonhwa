import sys
input = lambda: sys.stdin.readline().rstrip()

def hanoi(disk, s, m, e):
    if disk == 1:
        res.append(f'{s} {e}')
    else:
        hanoi(disk-1, s, e, m)
        res.append(f'{s} {e}')
        hanoi(disk-1, m, s, e)

n = int(input())
res = []
hanoi(n, 1, 2, 3)
print(len(res))
print('\n'.join(res))