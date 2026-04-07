try:
    numbers = [int(number) for number in input().split()]

    print('Среднее значение элементов:', sum(numbers)/len(numbers))

except ValueError:
    print('⚠️ Введите целые числа!')

except ZeroDivisionError:
    print('⚠️ Пустая строка!')