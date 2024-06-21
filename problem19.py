wk = 1
counter = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        # if sunday and first of month counter += 1
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            wk = (wk+31)%7
        elif month == 4 or month == 6 or month == 9 or month == 11:
            wk = (wk+30)%7
        else:
            if year%4 == 0:
                wk = (wk+29)%7
            else:
                wk = (wk+28)%7
        if wk == 0:
            counter += 1
            
print(counter)