with open ("C:/programacao/algorithms/numbers_million.txt", "r", encoding="utf-8") as numbers:
    numbers = [int(number) for line in numbers for number in line.split()]

def quick_sort(numbers:list, minimum:int, high:int):
    if minimum >= high:
        return
    pivo = numbers[high]
    barrier = minimum
    for x in range(minimum, high):
        if numbers[x] <= pivo:
            temp = numbers[x]
            numbers[x] = numbers[barrier]
            numbers[barrier] = temp
            barrier += 1

    temp = numbers[barrier]
    numbers[barrier] = numbers[high]
    numbers[high] = temp

    quick_sort(numbers, minimum, barrier-1)
    quick_sort(numbers, barrier+1, high)

    return numbers

print(quick_sort(numbers, 0, len(numbers)-1))
