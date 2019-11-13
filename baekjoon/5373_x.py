import pprint
def rotate(r, d):
    if r == 'U':
        # f -> l -> b -> r
        i = 0
        if d == 1:
            cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
            [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[3][2][2], cube[3][2][1], cube[3][2][0]] = [cube[3][2][2], cube[3][2][1], cube[3][2][0]], [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
            [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[5][2][0], cube[5][1][0], cube[5][0][0]] = [cube[5][2][0], cube[5][1][0], cube[5][0][0]] ,[cube[4][0][2], cube[4][1][2], cube[4][2][2]] 
            [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[2][0][0], cube[2][0][1], cube[2][0][2]] = [cube[2][0][0], cube[2][0][1], cube[2][0][2]] ,[cube[4][0][2], cube[4][1][2], cube[4][2][2]]
        else:
            cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
            [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[2][0][0], cube[2][0][1], cube[2][0][2]] = [cube[2][0][0], cube[2][0][1], cube[2][0][2]], [cube[4][0][2], cube[4][1][2], cube[4][2][2]] 
            [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[5][2][0], cube[5][1][0], cube[5][0][0]] = [cube[5][2][0], cube[5][1][0], cube[5][0][0]], [cube[4][0][2], cube[4][1][2], cube[4][2][2]] 
            [cube[4][0][2], cube[4][1][2], cube[4][2][2]], [cube[3][2][2], cube[3][2][1], cube[3][2][0]] = [cube[3][2][2], cube[3][2][1], cube[3][2][0]], [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
    elif r == 'D':
        i = 1
        if d == 1:
            cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
            [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[3][0][0], cube[3][0][1], cube[3][0][2]] = [cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
            [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[4][2][0], cube[4][1][0], cube[4][0][0]] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
            [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[2][2][2], cube[2][2][1], cube[2][2][0]] = [cube[2][2][2], cube[2][2][1], cube[2][2][0]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
        else:
            cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
            [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[2][2][2], cube[2][2][1], cube[2][2][0]] = [cube[2][2][2], cube[2][2][1], cube[2][2][0]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]] 
            [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[4][2][0], cube[4][1][0], cube[4][0][0]] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]] 
            [cube[5][0][2], cube[5][1][2], cube[5][2][2]], [cube[3][0][0], cube[3][0][1], cube[3][0][2]] = [cube[3][0][0], cube[3][0][1], cube[3][0][2]], [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
    elif r == 'F':
        i = 2
        if d == 1:
            # u -> r -> b -> l
            cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
            [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[0][2][2], cube[0][2][1], cube[0][2][0]] = [cube[0][2][2], cube[0][2][1], cube[0][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
            [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[5][2][2], cube[5][2][1], cube[5][2][0]] = [cube[5][2][2], cube[5][2][1], cube[5][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
            [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[1][2][2], cube[1][2][1], cube[1][2][0]] = [cube[1][2][2], cube[1][2][1], cube[1][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
        else:
            cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
            [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[1][2][2], cube[1][2][1], cube[1][2][0]] = [cube[1][2][2], cube[1][2][1], cube[1][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
            [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[5][2][2], cube[5][2][1], cube[5][2][0]] = [cube[5][2][2], cube[5][2][1], cube[5][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
            [cube[4][2][2], cube[4][2][1], cube[4][2][0]], [cube[0][2][2], cube[0][2][1], cube[0][2][0]] = [cube[0][2][2], cube[0][2][1], cube[0][2][0]], [cube[4][2][2], cube[4][2][1], cube[4][2][0]]
    elif r == 'B':
        i = 3
        if d == 1:
            cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
            [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[1][0][0], cube[1][0][1], cube[1][0][2]] = [cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
            [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[5][0][0], cube[5][0][1], cube[5][0][2]] = [cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
            [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[0][0][0], cube[0][0][1], cube[0][0][2]] = [cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
        else:
            cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
            [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[0][0][0], cube[0][0][1], cube[0][0][2]] = [cube[0][0][0], cube[0][0][1], cube[0][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
            [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[5][0][0], cube[5][0][1], cube[5][0][2]] = [cube[5][0][0], cube[5][0][1], cube[5][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
            [cube[4][0][0], cube[4][0][1], cube[4][0][2]], [cube[1][0][0], cube[1][0][1], cube[1][0][2]] = [cube[1][0][0], cube[1][0][1], cube[1][0][2]], [cube[4][0][0], cube[4][0][1], cube[4][0][2]]
    elif r == 'L':
        i = 4
        if d == 1:
            cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
            [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[3][2][0], cube[3][1][0], cube[3][0][0]] = [cube[3][2][0], cube[3][1][0], cube[3][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[0][2][0], cube[0][1][0], cube[0][0][0]] = [cube[0][2][0], cube[0][1][0], cube[0][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[2][2][0], cube[2][1][0], cube[2][0][0]] = [cube[2][2][0], cube[2][1][0], cube[2][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
        else:
            cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
            [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[2][2][0], cube[2][1][0], cube[2][0][0]] = [cube[2][2][0], cube[2][1][0], cube[2][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[0][2][0], cube[0][1][0], cube[0][0][0]] = [cube[0][2][0], cube[0][1][0], cube[0][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            [cube[1][0][2], cube[1][1][2], cube[1][2][2]], [cube[3][2][0], cube[3][1][0], cube[3][0][0]] = [cube[3][2][0], cube[3][1][0], cube[3][0][0]], [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
    elif r == 'R':
        i = 5
        if d == 1:
            cube[i] = [[cube[i][2][0],cube[i][1][0],cube[i][0][0]],[cube[i][2][1],cube[i][1][1],cube[i][0][1]],[cube[i][2][2],cube[i][1][2],cube[i][0][2]]]
            [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[3][0][2], cube[3][1][2], cube[3][2][2]] = [cube[3][0][2], cube[3][1][2], cube[3][2][2]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[1][2][0], cube[1][1][0], cube[1][0][0]] = [cube[1][2][0], cube[1][1][0], cube[1][0][0]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[2][0][2], cube[2][1][2], cube[2][2][2]] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        else:
            cube[i] = [[cube[i][0][2],cube[i][1][2],cube[i][2][2]],[cube[i][0][1],cube[i][1][1],cube[i][2][1]],[cube[i][0][0],cube[i][1][0],cube[i][2][0]]]
            [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[2][0][2], cube[2][1][2], cube[2][2][2]] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[1][2][0], cube[1][1][0], cube[1][0][0]] = [cube[1][2][0], cube[1][1][0], cube[1][0][0]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            [cube[0][0][2], cube[0][1][2], cube[0][2][2]], [cube[3][0][2], cube[3][1][2], cube[3][2][2]] = [cube[3][0][2], cube[3][1][2], cube[3][2][2]], [cube[0][0][2], cube[0][1][2], cube[0][2][2]]


T = int(input())
for t in range(T):
    n = int(input())
    # u - d - f - l - b - r
    cube = [
        [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
        [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
        [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
        [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
        [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
    ]
    l = list(input().split())
    for x in l:
        rotate(x[0], x[1])
    for i in range(3):
        print(''.join(cube[0][i]))
