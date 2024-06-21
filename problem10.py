import sympy
sum = 0


for i in range(1, 2000000):
    if sympy.isprime(i):
        sum += i
        
        
print(sum)