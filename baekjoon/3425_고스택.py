def calc(x):
    num = [x]
    for i in l:
        if i[:3] == 'NUM':
            num.insert(0, int(i[4:]))
        elif i == 'POP':
            if len(num) < 1:
                return 'ERROR'
            num.pop(0)
        elif i == 'INV':
            num[0] = -num[0]
        elif i == 'DUP':
            num.insert(0, num[0])
        elif i == 'SWP':
            if len(num) <= 1:
                return 'ERROR'
            num[0], num[1] = num[1], num[0]
        elif i == 'ADD':
            if len(num) <= 1:
                return 'ERROR'
            rnum = num.pop(1) + num.pop(0)
            if abs(rnum) > 10**9:
                return 'ERROR'
            num.insert(0, rnum)
        elif i == 'SUB':
            if len(num) <= 1:
                return 'ERROR'
            rnum = num.pop(1)-num.pop(0)
            if abs(rnum) > 10**9:
                return 'ERROR'
            num.insert(0, rnum)
        elif i == 'MUL':
            if len(num) <= 1:
                return 'ERROR'
            rnum = num.pop(0)*num.pop(0)
            if abs(rnum) > 10**9:
                return 'ERROR'
            num.insert(0, rnum)
        elif i == 'DIV':
            if len(num) <= 1 or num[0] == 0:
                return 'ERROR'
            if num[1] < 0:
                if num[0] < 0:
                    rnum = (-num.pop(1))//(-num.pop(0))
                else:
                    rnum = -((-num.pop(1))//num.pop(0))
            else:
                if num[0] < 0:
                    rnum = -(num.pop(1)//(-num.pop(0)))
                else:
                    rnum = num.pop(1)//num.pop(0)
            if abs(rnum) > 10**9:
                return 'ERROR'
            num.insert(0, rnum)
        elif i == 'MOD':
            if len(num) <= 1 or num[0] == 0:
                return 'ERROR'
            if num[1] < 0:
                if num[0] < 0:
                    rnum = -((-num.pop(1))%(-num.pop(0)))
                else:
                    rnum = -((-num.pop(1))%num.pop(0))
            else:
                if num[0] < 0:
                    rnum = num.pop(1)%(-num.pop(0))
                else:
                    rnum = num.pop(1)%num.pop(0)
            if abs(rnum) > 10**9:
                return 'ERROR'
            num.insert(0, rnum)
    if len(num) != 1:
        return 'ERROR'
    else:
        return num[0]


final = ''
while True:
    if final != '' and final != 'QUIT':
        l = [final]
    else:
        l = []
    while True:
        x = input()
        if x == 'END':
            break
        else:
            l.append(x)
    N = int(input())
    for _ in range(N):
        nums = int(input())
        res = calc(nums)
        print(res)
    print(input())
    final = input()
    if final == 'QUIT':
        break
