import sys
sys.stdin = open('1218.txt', 'r')

for t in range(10):
    N = int(input())
    bracket = [i for i in input()]
    checklist = []
    for i in bracket:
        if i == '{' or i == '[' or i == '(' or i == '<':
            checklist.append(i)
        elif i == '}' and checklist[-1] == '{':
            checklist.pop()
        elif i == ']' and checklist[-1] == '[':
            checklist.pop()
        elif i == ')' and checklist[-1] == '(':
            checklist.pop()
        elif i == '>' and checklist[-1] == '<':
            checklist.pop()
        elif i == checklist[-1]:
            break
        else:
            break
    if checklist:
        print(f'#{t+1} 0')
    else:
        print(f'#{t+1} 1')
        