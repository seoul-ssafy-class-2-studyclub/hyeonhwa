def check(a):
    checklist = []
    for i in a:
        if i == '(':
            checklist.append(i)
        if i == ')':
            checklist.pop(-1)
    if checklist:
        return False
    return True

a = '()()((()))'
b = '((()((((()()((()())((())))))'
print(check(a))
print(check(b))