def solution(arrangement):
    answer = 0
    lasor = []
    stick = []
    idx = 0
    reidx = 0
    for i in range(len(arrangement)-1):
        if arrangement[i] == '(' and arrangement[i+1] == ')':
            lasor.append([i, i+1])
        else:
            if arrangement[i] == '(':
                stick.append([i])
                idx += 1
            else:
                stick[idx].append(i)
                reidx = idx
                idx -= 1
    return answer