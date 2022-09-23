def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    change = 1
    for coin in coins:
        if change >= coin:
            change += coin
        else:
            break

    return change


coins = [5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(coins))

