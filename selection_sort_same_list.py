with open ("C:/PROG/facul/ex4/numbers.txt", "r", encoding="utf-8") as numbers:
    numbers = [int(number) for line in numbers for number in line.split()]

ordenado = False
actual_iteration = 0

while not ordenado:
    # Without auxiliar memory
    # inicial as numbers[actual_iteration], to atualizate every iteration
    min_number = [numbers[actual_iteration], actual_iteration]

    # Seaching the smallest number
    for i in range(actual_iteration, len(numbers)):
        if numbers[i] < min_number[0]:
            # Saving the number and the position
            min_number = [numbers[i], i]

    # Saving to exchange
    temp = numbers[actual_iteration]
    
    # exchange the actual_iteration with the min_number
    numbers[actual_iteration] = min_number[0]

    # Putting the before number in the min_number's place
    numbers[min_number[1]] = temp

    # Increasing the iteration
    actual_iteration += 1

    if actual_iteration == len(numbers):
        ordenado = True


print(numbers)