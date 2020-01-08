def solution(arrangement):
    answer = 0
    s = []
    for i in range(len(arrangement)):
        if i < len(arrangement) and arrangement[i] == '(' and arrangement[i+1] == ')':
            if s:
                answer += len(s)
        elif i >= 1 and arrangement[i-1] == '(' and arrangement[i] == ')':
            continue
        else:
            if arrangement[i] == '(':
                s.append(i)
                answer += 1
            else:
                s.pop()
    return answer

x = input()
print(solution(x))