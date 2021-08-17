1

num = input('Введите целое трехзначное число: ')

sum = 0
prod = 1

for i in num:
    sum += int(i)
    prod *= int(i)
print(f"sum : {sum}")
print(f"prod : {prod}")




2

a = 5
b = 6

print(f'{a} | {b} = {a | b}')
print(f'{a} >> {b} = {a >> b}')
print(f'{a} << {b} = {a << b}')
print(f'{a} & {b} = {a & b}')


3

x1, y1, x2, y2 = [
    int(x) for x in input('Введите координаты (x1 y1 x2 y2): ').split()
]
k = (y2 - y1)/(x2 - x1)
b= y1 - k * x1

print(f'y = {k}x + {b}')

4

import random

def is_float_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


a = input('Нижняя граница диапазона ')
b = input('Верхняя граница диапазона ')
result = None

if a.isdigit() and b.isdigit():
    result = random.randint(int(a), int(b))
elif is_float_number(a) and is_float_number(b):
    result = round(random.uniform(float(a), float(b)), 2)
elif a.isalpha() and b.isalpha():
    result = chr((random.randint(ord(a), ord(b))))

print(f'Результат {result}')

5

letter1, letter2 = [
    x.upper() for x in input('Введите две буквы через пробел (A - Z): ').split()
]


abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

index_letter1 = abc_list.index(letter1) + 1
index_letter2 = abc_list.index(letter2) + 1

if index_letter1 < index_letter2:
    step = 1
else:
    step = -1

print(f'Первая буква {letter1}, находится на позиции: {index_letter1}')
print(f'Вторая буква {letter2}, находится на позицииЖ {index_letter2}')
print(f'Между ними находятся буквы {abc_list[abc_list.index(letter1) + step:abc_list.index(letter2):step]}'
      f'{abs(index_letter1 - index_letter2) - 1})'
      )


6

abc_number = int(input('Введите номер буквы в алфавите '))

abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(abc_list)
if abc_number <= len(abc_list):
    print(f'Буква под номером {abc_number}: {abc_list[abc_number - 1]}')
else:
    print(f'Введенное число превышает количество букв в алфавите ({len(abc_list)}')



7

a = int(input('Длина первого отрезка '))
b = int(input('Длина второго отрезка '))
c = int(input('Длина третего отрезка '))

if a < b + c and b < a + c and c < a +b:
    if a == b and b == c:
        print(f'Треугольник равносторонний ')
    elif a == b or b == c or c == a:
        print(f'Треугольник равнобедренный ')
    else:
        print(f'Треугольник разносторонний ')
else:
    print(f'Такого треугольника не существует ')


8

year = int(input('Введите год: '))

if year % 400 == 0:
    print(f'Год высокосный ')
elif year % 100 == 0 and year % 400 != 0:
    print(f'Год не высокосный ')


9

n1, n2, n3 = [x for x in input('Введите три числа через пробел: ').split()]

if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Среднее: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Среднее: {n2}')
else:
    print(f'Среднее: {n3}')
