square_sum = lambda a : sum(range(1, a+1)) ** 2

sum_square = 0
for i in range(1, 101):
    sum_square += i**2

print(square_sum(100) - sum_square)