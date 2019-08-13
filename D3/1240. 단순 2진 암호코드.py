import sys
sys.stdin = open('1240.txt', 'r')

code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
T = int(input())
for t in range(T):
    N, M = input().split()
    key = [[i for i in input()] for j in range(int(N))]
    for i in key[:]:
        if '1' not in i[:]:
            key.remove(i)
    for j in range(int(M)):
        if ''.join(key[0][j:j+7]) in code and key[0][j+7] != '1':
            keys = ''.join(key[0][j:j+56])
            break
    result = []
    for i in range(0, len(keys), 7):
        result += [keys[i:i+7]]
    keycode = ''
    for res in result:
        keycode += str(code.index(res))
    mysum = (int(keycode[0])+int(keycode[2])+int(keycode[4])+int(keycode[6]))*3 + int(keycode[1]) + int(keycode[3]) + int(keycode[5]) + int(keycode[7])
    if mysum % 10 == 0:
        print('#{} {}'.format(t+1, int(keycode[0])+int(keycode[1])+int(keycode[2])+int(keycode[3])+int(keycode[4])+int(keycode[5])+int(keycode[6])+int(keycode[7])))
    else:
        print('#{} 0'.format(t+1))
