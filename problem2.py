a = 1
b = 2

sum = 2 

while a + b <= 4000000:
    if (a + b) % 2 == 0:
        sum += (a + b)
    c = a
    a = b
    b = c + b 
    
    
print(sum)