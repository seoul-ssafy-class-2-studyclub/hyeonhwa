def solution(clothes):
    def mul(arr):
        s = 1
        for i in arr:
            s *= i
        return s
    answer = 0
    kind = {}
    for i in clothes:
        if not kind.get(i[1]):
            kind[i[1]] = [i[0]]
        else:
            kind[i[1]].append(i[0])
    res = [0]*len(kind)
    idx = 0
    for value in kind.values():
        res[idx] = len(value)
        idx += 1
    if res.count(1) == len(res):
        return 2**len(res)-1
    for i in range(1 << len(res)):
        binary = []
        for j in range(len(res)):
            if i & (1 << j):
                binary.append(res[j])
        if binary:
            answer += mul(binary)
    return answer

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear'], ['tt', 'eyewear'], ['aa', 'body']]))