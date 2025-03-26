file = open("problem18.txt", "r")
nums = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

temp = list(map(int, file.read().split()))
count = 0
# assign values to a 2D list
for i in range(15):
    for j in range(15):
        if j <= i:
            nums[i].append(temp[count])
            count += 1

def getmax(ls, n, i, j):
    if n == 1:
        return ls[0][0]
    else:
        if j == 0:
            return ls[i][j] + getmax(ls[0:len(ls)-1], n-1, i-1, j)
        elif j == i:
            return ls[i][j] + getmax(ls[0:len(ls)-1], n-1, i-1, j-1)
        else:
            return max(ls[i][j] + getmax(ls[0:len(ls)-1], n-1, i-1, j), ls[i][j] + getmax(ls[0:len(ls)-1], n-1, i-1, j-1))


ans = []
for j in range(15):
    ans.append(getmax(nums, 15, 14, j))
  
print(max(ans))