l = [-7, -3, -2, 5, 8]
result = []
for i in range(1<<len(l)):
    a = []
    for j in range(len(l)):
        if i & (1<<j):
            a.append(l[j]) 
    result.append(a)
for i in result:
    if sum(i) == 0:
        print(True)
    else:
        print(False)
