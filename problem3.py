import sympy

def isprime(x):
    return sympy.isprime(x)

count = 0

for i in range (1, 775147):
    if 600851475143 % i == 0:
        if isprime(i):
            count = i
            
print(count)