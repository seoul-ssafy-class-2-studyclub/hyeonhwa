# def down()


N, M, H = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]
lines.sort(key=lambda x:x[0])