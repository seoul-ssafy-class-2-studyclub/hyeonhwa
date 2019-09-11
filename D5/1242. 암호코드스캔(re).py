import sys
sys.stdin = open('암호input.txt', 'r')

# dec = {'0110': 0, '1100': 1, '1001': 2, '1110': 3, '0001': 4, '1000': 5, '0111': 6, '1101': 7, '1011': 8, '0101': 9}
# h = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
#      '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
# for tc in range(1, int(input()) + 1):
#     r, c = map(int, input().split())
#     code = set()
#     inp = []
#     for _ in range(r):
#         temp = input().strip('0').split('00000')
#         for i in temp:
#             i = i.strip('0')
#             if i not in inp and i:
#                 inp.append(i)
#     for temp in inp:
#         for i in code:
#             temp = temp.replace(i, "")
#         temp = temp.strip('0')
#         code.add(temp)
#     real = set()
#     for cd in code:
#         for i in code:
#             if i != cd:
#                 cd = cd.replace(i, "")
#         real.add(cd)
#     result = 0
#     real -= {''}
#     for temp in real:
#         ans = ''
#         for i in temp:
#             ans += h[i]
#         t = len(ans) - 1
#         while ans[t] == "0":
#             t -= 1
#         ans = '0' * 15 + ans[:t + 1]
#         t = 1
#         while len(ans) >= t * 56:
#             t += 1
#         t -= 1
#         ans = ans[len(ans) - t * 56:]
#         if t > 1:
#             ans = "".join([ans[i] for i in range(0, len(ans), t)])
#         a = [dec[ans[i * 7:i * 7 + 7]] for i in range(8)]
#         odd = sum(a[i] for i in range(0, 7, 2))
#         even = sum(a[i] for i in range(1, 7, 2))
#         if (odd * 3 + even + a[7]) % 10 == 0:
#             result += odd + even + a[7]
#     print("#{} {}".format(tc, result))

def chk_code():
    global r, idx
    password = []
    mag = 0
    for i in range(8):
        ratio = [0, 0, 0, 0]
        while code[idx] != '0':
            ratio[3] += 1
            idx -= 1
        while code[idx] == '0':
            ratio[2] += 1
            idx -= 1
        while code[idx] != '0':
            ratio[1] += 1
            idx -= 1
        if not mag:
            mag = min(ratio[1], ratio[2], ratio[3])
        ratio[0] += (7 * mag) - sum(ratio)
        idx -= ratio[0]
        if mag > 1:
            ratio = map(lambda x: x // mag, ratio)
        password.insert(0, decode[tuple(ratio)])
    return password
  
  
hextobin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
  
decode = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4, (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8, (3, 1, 1, 2): 9}
  
result_list = []
for case in range(int(input())):
    N, M = map(int, input().split())
    codes = [list(input()) for _ in range(N)]
    binary = []
    visited = []
    result = 0
    code = []
    for i in codes:
        if i.count('0') != M and i not in code:
            code.append(i)
    for i in code:
        temp = ''
        k = M - 1
        while k >= 0:
            temp += hextobin[i[k]]
            k -= 1
        binary.append(temp)
    for cd in binary:
        idx = len(cd) - 1
        while idx >= 0:
            if cd[idx] != '0':
                password = chk_code()
                if password in visited:
                    continue
                chk = 0
                for i in range(8):
                    if not i % 2:
                        chk += password[i] * 3
                    else:
                        chk += password[i]
                if not chk % 10:
                    result += sum(password)
                    visited.append(password)
            else:
                idx -= 1
    result_list.append(result)
  
for i in range(len(result_list)):
    print(result_list[i])