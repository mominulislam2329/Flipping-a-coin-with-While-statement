import random  # random module will be imported

flip = 0
heads = 0
tails = 0
while flip <= 100:
    coin = random.randrange(2)
    if coin == 0:  # if 0 then heads
        heads += 1  # for counting number of heads
        print(heads, 'Head')

    else:
        tails += 1
        print(tails, 'tail')
    flip += 1

print('heads', heads)
print('tails', tails)
