left = 0
for i in range(1, 501):
    counter = 0
    for j in range(2, i+2):
        if j != i+1:
            counter += 2*(2**j)
        else:
            counter += 2**j
    left += 2*counter
    