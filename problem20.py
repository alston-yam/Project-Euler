def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

s = str(factorial(100))

sum = 0
for i in range(len(s)):
    sum += int(s[i])
    
print(sum)