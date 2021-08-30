import random

list = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {list}')

min_index = 0
max_index = 0
step = 1
sum = 0

for i in list:
    if list[min_index] > i:
        min_index = list.index(i)
    elif list[max_index] < i:
        max_index = list.index(i)

if max_index - min_index < 0:
    step = -1

for i in list[min_index + step:max_index:step]:
    sum += i
    # print(f'DEBUG i={i}')

print(
        f'Сумма элементов между минимальным ({list[min_index]})',
        f' и максимальным ({list[max_index]}) элементами: {sum}'
        )