# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое 
# число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3
new_list = ['gfh5', 'gfh2', '67', 'jy32', '3put']
number = '32'
for i in range(0, len(new_list)):
    a = new_list[i].find(number)
    # print(i, a)
    if a != -1:
        print(i)

# def find_element(my_list, num):
#     count = 0
#     switch = True

#     for i in my_list:
#         if i.find(num)!= -1:
#             print(f'{num}  содержится в элементе с индексом {count}')
#             switch = False
#         count+=1    
#     if switch:
#         print('элементов не найдено')


# my_list = ['gfh5', 'gfh2', '67', 'jy32', '3put', '56u32']
# num = input('введите искомый элемент: ')
# find_element(my_list, num)
