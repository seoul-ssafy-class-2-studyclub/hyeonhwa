def pal(a):
    if a == a[::-1]:
        return True
    else:
        return False

for t in range(10):
    n = int(input())
    l = []
    cnt = []
    for i in range(8):
        rows = input()
        l1 = [row for row in rows]
        l += [l1]
    l2 = [[l[i][j] for i in range(len(l))] for j in range(len(l))]
    for k in range(8):
        for i in range(8):
            for j in range(8-k+1): 
                if pal(l[i][j:j+k]) and k not in cnt:
                    cnt += [k]        
                if pal(l2[i][j:j+k]) and k not in cnt:
                    cnt += [k]  
    print('#{} {}'.format(t+1,cnt))
