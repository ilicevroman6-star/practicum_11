try:
    numbers = [int(number) for number in input().split()]

    if numbers.count(3) > 1:
        print('⚠️ Исходный список содержит значение 3 более одного раза!')
    elif numbers.count(3) < 1:
        print('⚠️ Исходный список не содержит значение 3!')
    else:
        numbers.remove(3)
        print(numbers)

except ValueError:
    print('⚠️ Введите целые числа!')