import sys
input = lambda: sys.stdin.readline().rstrip()

def check(a, b, num):
    ans = 0
    while queue:
        x = queue[-1]
        if x == a:
            return -1
        elif x == b:
            queue.pop()
            ans *= num
            queue.append(ans)
            break
        else:
            ans += queue.pop()
    return ans


arr = input()
queue = []
nums = []
for x in arr:
    if not queue:
        if x == ')' or x == ']':
            break
        queue.append(x)
    elif x == '(' or x == '[':
        queue.append(x)
    else:
        if x == ')':
            if queue[-1] == '(':
                queue.pop()
                queue.append(2)
            else:
                if check('[', '(', 2) == -1:
                    break
        elif x == ']':
            if queue[-1] == '[':
                queue.pop()
                queue.append(3)
            else:
                if check('(', '[', 3) == -1:
                    break
res = 0
for x in queue:
    if type(x) == int:
        res += x
    else:
        res = 0
        break
print(res)