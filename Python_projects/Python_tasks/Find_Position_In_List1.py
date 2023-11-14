# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

new_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find = 'qwe'
final_list = list(filter(lambda tup: tup[1] == find, enumerate(new_list)))
count = -1 if new_list.count(find) < 2 else final_list[1][0]
print(count)

# нумеруем изначальный список: получаем кортежи
# потом фильтруем: оставляем только те кортежи, второй элемент которых совпадает с искомой строкой
# заключаем всё это в список
# возвращаем -1, если строки нет, если есть - возвращаем первый элемент во втором кортеже нового списка

# Изначальное решение:
# new_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find = 'qwe'
# def func(new_list, find):
#     count = 0
#     n = -1
#     for i in range(0, len(new_list)):
#         a = new_list[i] == find
#         if a:
#             count+=1
#         if count == 2:
#             return i
#     return n
# print(func(new_list, find))


# решение преподавателя:
# find_second_occurence(string_list: List[str], search_word: str) -> int:
# try:
#     list_indexes = [index for index, string in enumerate(string_list) if string == search_word]
#     return list_indexes[0]
# except IndexError:
#     return -1