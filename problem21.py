#d(d(n)) = n

def d(n):
    counter = 0
    for i in range(1, n):
        if n%i == 0:
            counter += i
            
    return counter

num = 0
for i in range(1, 10000):
    k = d(i)
    if k != i and d(k) == i:
        print(i)
        num += i
        
print(num)