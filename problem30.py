# Max 7 degits
mylist=[]

for i in range(2, 1000000):
    if i == sum([int(x)**5 for x in str(i)]):
        mylist.append(i)
        
print(sum(mylist))