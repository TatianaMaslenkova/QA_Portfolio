# Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, 
# первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]
import random
size = 200
init_list = [random.randint(1, 100) for _ in range(0, size)]
print(init_list)
new_list = [(index, init_list[index]) for index in range(0, size) if index != init_list[index]]
print(f'Список кортежей:\n{new_list}\n')

# если через filter:
# import random
# size = 200
# init_list = [random.randint(1, 100) for _ in range(0, size)]
# print(init_list)
# new_list = list(filter(lambda i: i[0] != i[1], enumerate(init_list)))
# print(f'Список кортежей:\n{new_list}\n')