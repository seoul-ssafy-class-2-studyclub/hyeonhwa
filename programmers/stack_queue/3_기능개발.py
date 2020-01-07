import math

def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        progresses[i] = math.ceil((100 - progresses[i])/speeds[i])
    stack = []
    for i in  progresses:
        if not stack:
            stack.append(i)
        else:
            if stack[0] >= i:
                stack.append(i)
            else:
                answer.append(len(stack))
                stack = [i]
    answer.append(len(stack))
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 99], [4, 1]))