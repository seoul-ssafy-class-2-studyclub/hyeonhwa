T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()
    strlist = []
    cnt = 0
    for i in range(0, len(str2)-len(str1)+1):
        strlist += [str2[i:i+len(str1)]]
    for strs in strlist:
        if str1 == strs:
            cnt += 1

    print('#{} {}'.format(t+1, cnt))