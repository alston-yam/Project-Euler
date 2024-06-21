import math

def factorcount(num):
    count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0 and i != num/i:
            count += 2
        elif num % i == 0 and i == num/i:
            count += 1
            
    return count

tri = 0
i = 1

while True:
    tri += i
    i += 1
    amount = factorcount(tri)
    print(amount)
    if  amount > 500:
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        break

print(tri)