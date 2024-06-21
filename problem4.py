import math

def ispalindrome(x):
    counter = 0
    s = str(x)
    
    for i in range(math.ceil(len(s)/2)):
        if s[i] == s[len(s) - 1 - i]:
            counter += 1
    
    if counter == math.ceil(len(s)/2):
        return True
    else:
        return False    
    
    
large = 0
for i in range (100, 999):
    for j in range (100, 999):
        num = i * j
        if ispalindrome(num):
            large = max(num, large)

print(large)        