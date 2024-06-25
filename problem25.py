wow = []
stored = {1: 1, 2: 1}

def fib(n):
    if n in stored:
        return stored[n]
    else:
        stored[n] = fib(n-1) + fib(n-2)
        return stored[n]
        
    
l = []
for i in range(1, 9999999):
    k = fib(i)
    l.append(k)
    if len(str(k)) >= 1000:
        print(l.index(k)+1)
        break
