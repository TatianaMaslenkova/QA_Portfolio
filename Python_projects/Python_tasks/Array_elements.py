#  Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым 
#  значением. Пример: - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random
number = abs(int(input('Введите размер массива:\n')))
array = []
for i in range(number):
    array.append(random.randint(-10,11))
print(f'Исходный массив: {array}')
i = 0
for k in array:
    i+=1
    if k < 0:
        array.insert(i, 0)
        
print(f'Итоговый массив: {array}')

