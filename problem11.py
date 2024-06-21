file = open("problem11.txt", "r")
l = [ [] for _ in range(20)]
for i in range(20):
    l[i] = list(map(int, file.readline().split()))
file.close()

nums = []
for i in range(20):
    for j in range(0, 17):
        nums.append(l[i][j] * l[i][j+1] * l[i][j+2] * l[i][j+3])

for j in range(20):
    for i in range(0, 17):
        nums.append(l[i][j] * l[i+1][j] * l[i+2][j] * l[i+3][j])
        
for i in range(0, 17):
    for j in range(0, 17):
        nums.append(l[i][j] * l[i+1][j+1] * l[i+2][j+2] * l[i+3][j+3])

for i in range(0, 17):
    for j in range(3, 20):
        nums.append(l[i][j] * l[i+1][j-1] * l[i+2][j-2] * l[i+3][j-3])

print(l)
print(max(nums))