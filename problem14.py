k = []

for i in range(1, 999999):
    num = i 
    count = 0
    while num != 1:
        count += 1
        if num%2 == 0:
            num = num/2
        else:
            num = (3 * num) + 1
    print(count)
    k.append(count)
    
print(k.index(max(k)) + 1)