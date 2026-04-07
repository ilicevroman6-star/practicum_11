try:
    numbers = [int(number) for number in input().split()]

    command = input().strip()
    step = int(command[1:])

    if command[0] == 'R':
        new_numbers = numbers[-step:] + numbers[:-step]
    elif command[0] == 'L':
        new_numbers = numbers[step:] + numbers[:step]
    else:
        new_numbers = numbers.copy()

    print(new_numbers)

except ValueError:
    print('⚠️ Введите целые числа!')