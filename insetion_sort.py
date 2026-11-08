with open ("C:/PROG/facul/algorithms/numbers.txt", "r", encoding="utf-8") as numbers:
    numbers = [int(number) for line in numbers for number in line.split()]

for index in range(0, len(numbers)):
    
    for y in range(index, 0, -1):

        if numbers[y] < numbers[y - 1]:
            temp = numbers[y - 1]
            numbers[y - 1] = numbers[y]
            numbers[y] = temp
        else:
            break

print(numbers)