import random
def dice():
    numbers = ['one', 'two', 'three', 'four', 'five', 'six']

    result = random.choice(dice)

    pro = dice.count('one')/len(dice)
    print("Probability of picking one is:", pro)

    if result == 'one':
        return 'one was picked'
    else:
        return 'better luck next time'

res = dice()
print(res)