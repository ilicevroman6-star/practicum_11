try:
    numbers = [int(input()) for _ in range(10)]

    numbers_new = [numbers[i-1] + numbers[i+1] for i in range(len(numbers))
                   if i != 0 and i != 9]

    print(numbers_new)

except ValueError:
    print('⚠️ Введите целые числа!')