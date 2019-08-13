import sys
sys.stdin = open('1289.txt', 'r')

T = int(input())
for t in range(T):
    original = [i for i in input()]
    copy = ['0' for i in range(len(original))]
    cnt = 0
    for i in range(len(original)):
        if original[i] != copy[i]:
            copy[i:len(copy)] = [original[i] for j in range(len(copy)-i)]
            cnt += 1
        if copy == original:
            break
    print('#{} {}'.format(t+1, cnt))
