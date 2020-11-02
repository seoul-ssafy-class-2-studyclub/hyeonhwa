for t in range(int(input())):
    n = int(input())
    people = list(map(int, input().split()))
    avg = sum(people)/len(people)
    res = 0
    for p in people:
        if p <= avg:
            res += 1
    print(res)
