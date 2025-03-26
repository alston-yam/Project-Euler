mylist = []

for a in range(2, 101):
    for b in range(2, 101):
        mylist.append(a**b)

print(len(set(mylist)))