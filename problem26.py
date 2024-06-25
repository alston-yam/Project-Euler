cycles = [0]

for d in range(1, 1000):
    if d%2 != 0 and d%5 != 0:
        n = 1
        broken = False
        while True:
            for j in range(0, n):
                if (10**n - 10**j)%d == 0:
                    broken = True
                    cycles.append(n-j)
                    break
            if broken:
                break
            n += 1
    else:
        cycles.append(0)
        
    print(cycles)

print(cycles.index(max(cycles)))