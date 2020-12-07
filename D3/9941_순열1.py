for t in range(int(input())):
    n = int(input())
    l = [int(i) for i in input()]
    l.sort()
    for i in range(n-1):
        if l[i] == l[i+1]:
            print(f'#{t+1} No')
            break
    print(f'#{t+1} Yes')
