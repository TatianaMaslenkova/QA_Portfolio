# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих 
# на нечётной позиции. Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
def fill_list(n_list: list, n: int) -> list:
    '''
    Возвращает список, заполненный случайными числами

        Args:
            n_list (list) - список
            n (int) - число, которое задаёт пользователь, которое определяет размер списка  
        Returns:
            n_list (list) - список, заполненный случайными числами
    '''
    for i in range(0, n):
        n_list.append(random.randint(-10, 10))
    print(n_list)

# print(fill_list.__doc__) # для вывода в консоль информации, содержащейся в docstring

def odd_position_numbers_sum(n_list: list) -> int:
    '''
    Вычисляет сумму элементов, стоящих на нечётных позициях в списке

        Args:
            n_list (list) - список  
        Returns:
            sum (int) - сумма элементов, стоящих на нечётных позициях в списке 
    '''
    sum = 0
    for i in range(1, len(n_list), 2):
        sum += n_list[i]
    return sum

# print(odd_position_numbers_sum.__doc__) # для вывода в консоль информации, содержащейся в docstring
        
size = abs(int(input('Количество чисел в списке: ')))
new_list = []

fill_list(new_list, size)
res = odd_position_numbers_sum(new_list)
print(f'Сумма элементов, стоящих на нечётных позициях, равна {res}')