import random

list_1 = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {list_1}')

min_index_1 = 0
min_index_2 = 1

for i in list_1:
    if list_1[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = list_1.index(i)
    elif list_1[min_index_2] > i:
        min_index_2 = list_1.index(i)

print(f'Два наименьших элемента: {list_1[min_index_1]} и {list_1[min_index_2]}')

