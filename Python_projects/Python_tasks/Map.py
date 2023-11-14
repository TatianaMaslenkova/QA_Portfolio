# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие. [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

init_list = list(map(int, input("Введите числа через пробел: ").split()))
print(init_list)
new_list = []
[new_list.append(i) for i in init_list if i not in new_list]
print(new_list)

# Изначальное решение, которое сократила до итогового (которое приведено выше): 
# numbers = input("Введите числа через пробел: ")
# init_list = list(map(int, numbers.split()))
# print(init_list)
# new_list = []
# for i in init_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)