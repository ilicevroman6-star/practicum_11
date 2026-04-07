try:
    number = int(input())
    dividers = [divider for divider in range(number, 0, -1)
                if number % divider == 0]

    print(dividers)

except ValueError:
    print('⚠️ Введите целое число!')