print('Welcome to Even Odd Number Sorter App')

repeat = True
while repeat:
    numbers = input('Enter numbers separated by commas: ')
    numbers = numbers.replace(" ", "")
    num_list = numbers.split(',')
    evens = []
    odds = []

    print('\t--Result Summary')
    for num in num_list:
        num = int(num)
        if num % 2 == 0:
            print(f'\t{num} is Even number')
            evens.append(num)
        else:
            print(f'\t{num} is Odd number')
            odds.append(num)
    evens.sort()
    odds.sort()

    print(f'The following numbers {len(evens)} are Even numbers: ')
    for even in evens:
        print(f'\t{even}')

    print(f'The following numbers {len(odds)} are Odd numbers: ')
    for odd in odds:
        print(f'\t{odd}')
    choice = input('Do you want to try again?(y/n): ').lower().strip()
    if choice.startswith('n'):
        repeat = False
        print('Thank you for using the App')
