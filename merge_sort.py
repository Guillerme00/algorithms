with open ("C:/PROG/facul/algorithms/numbers_million.txt", "r", encoding="utf-8") as numbers:
    numbers = [int(number) for line in numbers for number in line.split()]

def join_list(list1:list, list2: list):
    organized = False
    lista = []
    index1 = 0
    index2 = 0
    while not organized:
        if len(list1) != index1 and len(list2) != index2: 
            if list1[index1] < list2[index2]:
                lista.append(list1[index1])
                index1 += 1
            else:
                lista.append(list2[index2])
                index2 += 1
        else:
            if len(list1) == index1:
                lista = lista + list2[index2:]
                organized = True
            else:
                lista = lista + list1[index1:]
                organized = True
    return lista

def split_list(lista: list):
    if len(lista) <= 1:
        return lista
    
    half = len(lista)//2

    first_half = split_list(lista[:half])
    second_half = split_list(lista[half:])

    return join_list(first_half, second_half)

print(split_list(numbers))