def solution(answers):
    ans = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        answer = answers[i]
        if answer == one[i%5]:
            ans[0] += 1
        if answer == two[i%8]:
            ans[1] += 1
        if answer == three[i%10]:
            ans[2] += 1
    res = []
    x = max(ans)
    for i in range(len(ans)):
        if ans[i] == x:
            res.append(i+1)
    return res