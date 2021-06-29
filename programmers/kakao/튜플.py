def solution(s):
    tus = []
    tu = []
    st = ""
    for i in range(1, len(s)-1):
        if s[i].isdigit():
            st += s[i]
        elif s[i] == "," and st:
            tu.append(int(st))
            st = ""
        elif s[i] == "}":
            tus.append(tu + [int(st)])
            st = ""
            tu = []
    tus.sort(key=lambda x:len(x))
    res = []
    for t in tus:
        for x in t:
            if x not in res:
                res.append(x)
    return res

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
