for t in range(10):
    N = int(input())
    n = 100
    rows = [[i for i in input().split()] for j in range(n)]
    rows = list(map(list,zip(*rows)))
    cnt = 0
    for row in rows[:]:
        if row.count('1') + row.count('2') == 1 or row.count('0') == n:
            rows.remove(row)
        for i in range(row.count('0')):
            row.remove('0')
    cnt = 0
    for row in rows:
        for i in range(len(row)-1):
            if row[i] == '1' and row[i+1] == '2':
                cnt += 1
    print('#{} {}'.format(t+1, cnt))