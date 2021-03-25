# 분할정복
def stars(x):
    mat = []
    for i in range(3*len(x)):
        if i // len(x) == 1:
            mat.append(x[i%len(x)] + ' '*len(x) + x[i%len(x)])
        else:
            mat.append(x[i%len(x)]*3)
    return(mat)


n = int(input())
k = 0
star = ['***', '* *', '***']
while n != 3:
    n = n//3
    k += 1
for i in range(k):
    star = stars(star)
for i in star:
    print(i)
