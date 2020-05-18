n = int(input())
people = list(map(int, input().split()))
res = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == people[i]:
            break
        if res[j] == 0:
            cnt += 1
    if res[j] == 0:
        res[j] = i+1
    else:
        while res[j] != 0:
            j += 1
        res[j] = i+1
print(' '.join(list(map(str, res))))