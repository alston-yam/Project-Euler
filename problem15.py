l = [[0 for x in range(21)] for y in range(21)]
for i in range(21):
    l[0][i] = 1
    l[i][0] = 1

for i in range(1, 21):
    for j in range(1, 21):
        l[i][j] = l[i-1][j] + l[i][j-1]

print(l)
print(l[20][20])
