# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Пример: для 
# k = 8 список будет выглядеть: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def nega_fib(fib_l: list, count: int) -> list:
    '''
    Возвращает список чисел Фибоначчи, в том числе для отрицательных индексов

        Args:
            fib_l (list) - список первых отрицательно и положительно индексированных эл-ов последовательности
            count (int) - число, которое ввёл пользователь
        Returns:
            fib_l (list) -  список чисел Фибоначчи для положительных и отрицательных индексов
    '''
    new_len = len(fib_l)
    if new_len >= count * 2:
        return fib_l
    fib_l.append(fib_l[new_len - 1] + fib_l[new_len - 2])
    fib_l.insert(0, (-1) ** (new_len // 2) * fib_l[new_len])
    nega_fib(fib_l, count)
    return fib_l

num = int(input('Введите количество чисел Фибоначчи: '))
fib_list = [1, 0, 1]
print(nega_fib(fib_list, num))

# Эталонное решение от преподавателя:
# def get_fibonacci(n):
#     fibo_num = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_num.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_num.insert(0, a)
#         a, b = b, a - b
#     return fibo_num
