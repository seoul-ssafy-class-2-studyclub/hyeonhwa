def calculate(a, b, c):
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    else:
        return a*b

def solution(expression):
    ex = []
    st = ""
    for i in expression:
        if i == "-" or i == "+" or i == "*":
            ex.append(int(st))
            st = ""
            ex.append(i)
        else:
            st += i
    ex.append(int(st))
    sign = ["+", "-", "*"]
    visit = [0]*3
    pri_sign = []
    def pri(arr):
        if len(arr) == 3:
            pri_sign.append(arr)
            return
        for i in range(3):
            if not visit[i]:
                visit[i] = 1
                pri(arr+[sign[i]])
                visit[i] = 0
    pri([])
    res = 0
    for s in pri_sign:
        i = 0
        cal = []
        j = 0
        while j < len(ex):
            if ex[j] == s[i]:
                num = calculate(cal.pop(), ex[j+1], s[i])
                cal.append(num)
                j += 1
            else:
                cal.append(ex[j])
            j += 1
        i += 1
        while i < 3:
            cals = []
            j = 0
            while j < len(cal):
                if cal[j] == s[i]:
                    num = calculate(cals.pop(), cal[j+1], s[i])
                    cals.append(num)
                    j += 1
                else:
                    cals.append(cal[j])
                j += 1
            cal = cals
            i += 1
        res = max(res, abs(cal[0]))
    return res
                

solution("100-200*300-500+20")
