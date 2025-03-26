# 1p 2p 5p 10p 20p 50p 100p 200p

#make 200p


# 200
# 100 100
# 100 50 50
# 100 50 20 20 10
# 100 50 20 20 5 5
# 100 50 20 20 5 2 2 1
# 100 50 20 20 5 2 1 1 1
# 100 50 20 20 5 1 1 1 1 1

# To make 5p there's 4 ways
# to make 200p there's 73682 ways

def make_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0
    return make_change(amount - coins[0], coins) + make_change(amount, coins[1:])

print(make_change(200, [1, 2, 5, 10, 20, 50, 100, 200]))