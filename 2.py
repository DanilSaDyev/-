def find_triples(lst):
    result = []
    for i in range (len(lst) - 2):
        if lst[i] < lst[i+1] > lst[i+2]:
            result .appened((i, i+1, i+2))
        return result 
numbers = [3, 4, 6, 8, 3, 2, 9, 6]
triples = find_triples(numbers)
if triples:
    print("Найдены тройки соседних чисел, удовлетворяющие условию:")
    for triples in triples:
        print("Тройка", 
numbers[triple[0]],
numbers[triple[1]],
numbers[triple[2]])
else:
    print("В массиве отсутствуют тройки удовлетворяющие условию.")
