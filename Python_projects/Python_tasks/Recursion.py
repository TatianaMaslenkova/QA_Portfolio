# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно 
# решить с помощью рекурсии. Не использовать функцию bin. Пример: 45 -> 101101 3 -> 11 2 -> 10

def from_dec_to_bin(dec_num: int, bin_num: str) -> str:
    '''
    Возвращает перевёрнутую строку результата деления числа на 2 (что и есть двоичное число)

        Args:
            dec_num (int) - число, которое задаёт пользователь
            bin_num (str) - пустая строка
        Returns:
            bin_num (str) - перевёрнутая строка результата деления числа на 2
    '''
    if dec_num != 0:
        bin_num += from_dec_to_bin(dec_num // 2, bin_num) + str(dec_num % 2)
    return bin_num

decimal_num = abs(int(input('Введите число: ')))
bin_num = ''
bin_num = from_dec_to_bin(decimal_num, bin_num)
print(bin_num)


# Без рекурсии:
# def from_dec_to_bin(dec_num: int, bin_num: str) -> str:
#     '''
#     Возвращает перевёрнутую строку результата деления числа на 2 (что и есть двоичное число)

#         Args:
#             dec_num (int) - число, которое задаёт пользователь
#             bin_num (str) - пустая строка
#         Returns:
#             res (str) - перевёрнутая строка результата деления числа на 2
#     '''
#     while dec_num > 0:
#         bin_num += str(dec_num % 2)
#         dec_num = dec_num // 2
#         res = bin_num[::-1]
#     print(res)

# decimal_num = abs(int(input('Введите число: ')))
# bin_num = ''
# from_dec_to_bin(decimal_num, bin_num)