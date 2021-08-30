list = [2, 5, 6, 7, 8, 9, 1, 2, 4]

max_index = 0
min_index = 0

for index in range(len(list)):
    if list[index] > list[max_index]:
        max_index = index
    elif list[index] < list[min_index]:
        min_index = index

list[max_index], list[min_index] = list[min_index], list[max_index]
print(list)