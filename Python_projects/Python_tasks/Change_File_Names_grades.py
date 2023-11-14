# В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл. Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4
from typing import List
def read_file(filename: str) -> List[str]:
    '''
    Возвращает список, заполненный строками файла (1 элемент списка = 1 строка в файле)

        Args:
            filename (str) - исходный файл
        Returns:
            new_list (List[int]) - список, заполненный строками исходного файла
    '''
    with open(filename, 'r',encoding='UTF8') as file:
        new_list = [] 
        for i in file:
            new_list.append(i.rstrip())
    return new_list

def upper_case(new_list: List[str], grade: str) -> List[str]:
    '''
    Возвращает список, в котором элементы, содержащие искомый символ, прописаны заглавными буквами, остальные элементы оставлены без изменений

        Args:
            filename (str) - исходный файл
            grade (str) - искомый символ, наличие которого требует изменения элемента
        Returns:
            new_list (List[int]) - список, в котором заглавными буквами написаны элементы, содержащие искомый символ, остальные элементы оставлены без изменений
    '''
    for i in range(0,len(new_list)):    
        if new_list[i].count(grade):
            new_list[i] = new_list[i].upper()
    return new_list         

def rewrite_to_file(new_list: List[str],filename: str) -> str:
    '''
    Записывает в файл новые данные

        Args:
            new_list (List[int]) - изменённый список
            filename (str) - файл
        Returns:
            str - строка с изменёнными данными
    '''
    with open(filename, 'w', encoding='UTF8') as file:
        for i in new_list:    
            file.write(f'{i}\n')

file = 'Names_grades.txt'
print(type(file))
full_list = read_file(file)
print(full_list)
rewrite_to_file(upper_case(full_list, '5'), file)
