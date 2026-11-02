ordened_list = []

with open ("C:/PROG/facul/ex4/numbers.txt", "r", encoding="utf-8") as numbers:
    numbers = [int(number) for line in numbers for number in line.split()]

while numbers:
    # With auxiliar memory
    # inicial as numbers[0]
    min_number = [numbers[0], 0]

    # Seaching the smallest number
    for i in range( 0, len(numbers)):
        if numbers[i] < min_number[0]:
            # Saving the number and the position
            min_number = [numbers[i], i]

    #Saving the new smallest in the final position
    ordened_list.append(min_number[0])

    # Pop the smallest
    numbers.pop(min_number[1])
