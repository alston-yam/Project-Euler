# n^2 +an + b 

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

counter = 0
prev = 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        for n in range(abs(b)):
            if is_prime(n**2 + a*n + b):
                counter += 1
            else:
                break
        if counter > prev:
            prev = counter
            prod = a*b
        counter = 0
print(prod)