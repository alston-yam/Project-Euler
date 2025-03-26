file = open("problem67.txt", "r")
nums = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

temp = list(map(int, file.read().split()))
count = 0
# assign values to a 2D list
for i in range(100):
    for j in range(100):
        if j <= i:
            nums[i].append(temp[count])
            count += 1

ex = [[False for _ in range(100)] for _ in range(100)]
val = [[0 for _ in range(100)] for _ in range(100)]
ex[0][0] = True
val[0][0] = nums[0][0]

def getmax(ls, n, i, j):
    if n == 1:
        return ls[0][0]
    else:
        if j == 0:
            if ex[i-1][j] == False:
                ex[i-1][j] = True
                val[i-1][j] = getmax(ls[0:len(ls)-1], n-1, i-1, j)
            
            ex[i][j] = True
            val[i][j] = ls[i][j] + val[i-1][j]
        elif j == i:
            if ex[i-1][j-1] == False:
                ex[i-1][j-1] = True
                val[i-1][j-1] = getmax(ls[0:len(ls)-1], n-1, i-1, -1)

            ex[i][j] = True
            val[i][j] = ls[i][j] + val[i-1][j-1]
        else:
            if ex[i-1][j] == False:
                ex[i-1][j] = True
                val[i-1][j] = getmax(ls[0:len(ls)-1], n-1, i-1, j)
            if ex[i-1][j-1] == False:
                ex[i-1][j-1] = True
                val[i-1][j-1] = getmax(ls[0:len(ls)-1], n-1, i-1, j-1)
            
            ex[i][j] = True
            val[i][j] = max(ls[i][j] + val[i-1][j], ls[i][j] + val[i-1][j-1])
            # return max(ls[i][j] + getmax(ls[0:len(ls)-1], n-1, i-1, j), ls[i][j] + getmax(ls[0:len(ls)-1], n-1, i-1, j-1))
        
        return val[i][j]

ans = []
for j in range(100):
    ans.append(getmax(nums, 100, 99, j))
print(max(ans))