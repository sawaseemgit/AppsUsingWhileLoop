import random

print('Welcome to Power-ball Simulator')
whites = int(input('How many white-balls to draw from for the 5 winning numbers(Usually 69): '))
if whites < 5:
    whites = 5
reds = int(input('How many red-balls to draw from for the Power-ball(Usually 26): '))
if reds < 1:
    reds = 1

odds = 1
for i in range(5):
    odds *= whites - i
odds *= reds / 120
print(f'You have a 1 in {odds} chances of winning the lottery.')

tckt_interval = int(input('Purchase tickets in what interval: '))
winning_numbers = []
while len(winning_numbers) < 5:
    number = random.randint(1, whites)
    if number not in winning_numbers:
        winning_numbers.append(number)
winning_numbers.sort()
number = random.randint(1, reds)
winning_numbers.append(number)
print(winning_numbers)
print('********Welcome to the Power-Ball*********')
print('Todays winning numbers are: ', end='')
for number in winning_numbers:
    print(f'{number}', end=' ')

input('Press Enter to start purchasing tickets.')
tckt_purchased = 0
active = True
tckt_sold = []

while winning_numbers not in tckt_sold and active == True:
    lottery_numbers = []
    while len(lottery_numbers) < 5:
        number = random.randint(1, whites)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    lottery_numbers.sort()

    number = random.randint(1, reds)
    lottery_numbers.append(number)

    if lottery_numbers not in tckt_sold:
        tckt_purchased += 1
        tckt_sold.append(lottery_numbers)
        print(lottery_numbers)

    else:
        print('Loosing ticket generated, disregard...')

    if tckt_purchased % tckt_interval == 0:
        print(f'{tckt_purchased} tickets purchased so far with no winners...')
        choice = input('Keep purchasing tickets?(Yes/No): ').lower().strip()
        if choice.startswith('n'):
            active = False

if lottery_numbers == winning_numbers:
    print('Winning ticket numbers: ', end='')
    for number in lottery_numbers:
        print(f'{number}', end='')
    print(f'Purchased a total of {tckt_purchased} tickets.')

else:
    print(f'You bought {tckt_purchased} and still lost.Better luck next time.')
