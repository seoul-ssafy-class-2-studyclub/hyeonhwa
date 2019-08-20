row, col = map(int, input().split())
cuts = []
for i in range(int(input())):
    cuts.append(list(map(int, input().split())))
cols, rows = [0], [0]
for i in cuts:
    if i[0] == 0:
        cols += [i[1]]
    else:
        rows += [i[1]]
cols = sorted(cols)
rows = sorted(rows)

cols.append(col)
col_sd = cols[0]
for i in range(1, len(cols)):
    if col_sd < cols[i] - cols[i-1]:
        col_sd = cols[i] - cols[i-1]

rows.append(row)
row_sd = rows[0]
for i in range(1, len(rows)):
    if row_sd < rows[i] - rows[i-1]:
        row_sd = rows[i] - rows[i-1]

print(row_sd * col_sd)