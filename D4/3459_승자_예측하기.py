result = []
for t in range(int(input())):
    N = int(input())
    x = 1
    res = 'Alice'
    while N > 0:
        N -= x
        if res == 'Alice':
            x *= 4
            res = 'Bob'
        else:
            res = 'Alice'
    result.append(f'#{t+1} {res}')
print('\n'.join(result))
