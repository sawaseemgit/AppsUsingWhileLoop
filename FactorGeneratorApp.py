print('Welcome to the Factor Generator App')

repeat = True
while repeat:
    number = int(input('Enter a number to determine all factors of: '))
    factors = []
    print(f'The factors of {number} are:')
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
            print(f'\t{i}')

    print('In summary: ')
    for i in range(len(factors) // 2):
        print(f'\t{factors[i]}*{factors[-i - 1]}=', factors[i] * factors[-i - 1])

    choice = input('Do you want to run again?(y/n):').lower().strip()
    if choice.startswith('n'):
        repeat = False
        print('Thank you for using the App.')
