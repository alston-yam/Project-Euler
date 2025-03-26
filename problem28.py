sum = 1
temp = 3
for i in range(2, 1001, 2):
    for j in range(4):
        sum += temp
        if j != 3:
            temp += i
        else:
            temp += i + 2
        print(sum, temp)
        
    
print(sum)