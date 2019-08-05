# import random
# l = [[i for i in random.sample(range(1, 26), 5)] for j in range(5)]
l = [[1, 1, 1, 1, 1 ], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
print(l)
l.insert(0,l[0])
l.insert(len(l), l[-1])
for i in range(1, len(l)-1):
    l[i].insert(0, l[i][0])
    l[i].insert(len(l), l[i][-1])
sums = []
for i in range(1, len(l)-1):
    for j in range(1, len(l)-1):
        sums += [abs(l[i][j]-l[i-1][j]) + abs(l[i][j]-l[i+1][j]) + abs(l[i][j]-l[i][j-1]) + abs(l[i][j]-l[i][j+1])]
print(sums)