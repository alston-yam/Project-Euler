def d(n):
    counter = 0
    for i in range(1, n):
        if n%i == 0:
            counter += i
            
    return counter

abundant = []
for i in range(1, 28124):
    k = d(i)
    if k > i:
        print(i, k)
        abundant.append(i)

print(len(abundant))

sum = [0] * 28124
for i in range(0, len(abundant)):
    for j in range(i, len(abundant)):
        sum2 = abundant[i] + abundant[j]
        if sum2 <= 28123 and sum[sum2] == 0:
            sum[sum2] = sum2

print(sum)

total = 0
for i in range(1, len(sum)):
    if sum[i] == 0:
        total += i
        
print(total)