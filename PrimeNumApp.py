import datetime

print('Welcome to the Prime Numbers App')
repeat = True
while repeat:

    option = int(input('Enter 1 to find if a number is prime.\nEnter 2, to find out '
                       'if all numbers in a set are prime.\nEnter your choice: '))

    if option == 1:
        number = int(input('Enter a number: '))
        prime_status = True
        for i in range(2, number):
            if number % i == 0:
                prime_status = False
                break

        if prime_status:
            print(f'{number} is a prime number')
        else:
            print(f'{number} is not a prime number')


    elif option == 2:
        l_bound = int(input('Enter lower bound of your range: '))
        u_bound = int(input('Enter upper bound of your range: '))
        primes = []
        start_time = datetime.datetime.now()
        for p in range(l_bound, u_bound + 1):
            if p > 1:
                prime_status = True
                for i in range(2, p):
                    if p % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False
            if prime_status:
                primes.append(p)
        end_time = datetime.datetime.now()
        del_time = round((end_time - start_time).total_seconds(), 6)
        print(f'Calculation took {del_time} seconds time to print.\nThe following numbers between '
              f'{l_bound} and {u_bound} are prime: ')
        input('Press Enter to continue.')
        print(primes)

    else:
        print('That is not a valid choice.')

    choice = input('Would you like to run again?(yes/no): ').lower().strip()
    if choice.startswith('n'):
        repeat = False
