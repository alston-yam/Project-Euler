for a in range (1, 1000):
    for b in range(1, 1000):
        if a + b >= 1000:
            break
        else:
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                am = a
                bm = b
                cm = c
                break 

print(am * bm * cm)