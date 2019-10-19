N = int(input())
board = list(map(int, input().split()))
B, C = map(int, input().split())
res = 0
for i in board:
    if i <= B:
        res += 1
    else:
        res += 1
        if (i-B)%C == 0:
            res += (i-B)//C
        else:
            res += (i-B)//C+1
print(res)