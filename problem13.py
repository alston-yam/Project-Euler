file = open("problem13.txt", "r")
l = [[] for _ in range(100)]
for i in range(100):
    l[i] = list(map(int, file.readline().split()))
    
k = 0
for i in l:
    k += i[0]

k = str(k)

s = ""
for i in range(10):
    s += k[i]

print(s)