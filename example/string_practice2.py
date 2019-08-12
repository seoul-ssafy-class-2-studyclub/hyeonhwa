# a = 1234
# result = ''
# for i in range(3, -1, -1):
#     result += '{}'.format(a // (10**i))
#     a -= a//(10**i)*(10**i)
# print(result)

def itoa(x):
    sr=''
    while True:
        r = x%10
        sr = sr + chr(r + ord('0'))
        x //= 10
        if x == 0:
            break
    s = ''
    for i in range(len(sr)-1, -1, -1):
        s = s + sr[i]

    return s

print(itoa(1234))