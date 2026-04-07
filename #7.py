try:
    numbers = [int(number) for number in input().split()]

    # even - чётные, odd - нечётные
    sum_even = sum_odd = 0

    for number in numbers:
        if number % 2 == 0:
            sum_even += number

        else:
            sum_odd += number

    print('Сумма чётных:', sum_even)
    print('Сумма нечётных:', sum_odd)

except ValueError:
    print('⚠️ Введите целые числа!')