try:
    numbers_1 = [int(number) for number in input().split()]
    numbers_2 = [int(number) for number in input().split()]
    start = int(input())
    end = int(input())

    for i in range (end - 1, start - 2, -1):
        numbers_2.append(numbers_1[i])
        numbers_1.pop(i)

    print(numbers_1)
    print(numbers_2)

except ValueError:
    print('⚠️ Введите целые числа!')

except IndexError:
    print('⚠️ Неправильно выбран диапазон!')