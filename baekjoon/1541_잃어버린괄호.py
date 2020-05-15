import sys
input = lambda: sys.stdin.readline().rstrip()

# expression = [i for i in input()]
# flag = 0
# res = ''
# for ex in expression:
#     if ex == '-':
#         if flag == 0:
#             res += '-('
#             flag = 1
#         else:
#             res += ')-('
#     else:
#         if ex == '0' and (not res or not res[-1].isdigit()):
#             continue
#         res += ex
# if flag == 1:
#     res += ')'
# # print(res)
# print(eval(res))

expression = input().split('-')
res = 0
for i in range(len(expression)):
    ex = expression[i].split('+')
    if i == 0:
        res += sum(list(map(int, ex)))
    else:
        res -= sum(list(map(int, ex)))
print(res)
