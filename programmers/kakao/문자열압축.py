def solution(s):
    ans = len(s)
    for i in range(1, len(s)//2+1):
        res = []
        x, cnt = s[:i], 1
        for j in range(i, len(s), i):
            if x == s[j:j+i]:
                cnt += 1
            else:
                res.append((x, cnt))
                x, cnt = s[j:j+i], 1
        res.append((x, cnt))
        num = 0
        for x, cnt in res:
            if cnt == 1:
                num += len(x)
            else:
                num += len(x) + len(str(cnt))
        ans = min(ans, num)
    return ans

solution("xxxxxxxxxxyyy")
