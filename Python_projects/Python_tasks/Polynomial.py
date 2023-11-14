# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 
# 100) многочлена и записать в файл многочлен степени n. Пример:
# - n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 (коэф: []) или 10*x² = 0

# Уточнения:
# n - это степень икса первого элемента полинома
# при n =3 => 5*x*3 + 18*x**2 + 7*x + 19 = 0 - коэффициенты = [5,18,7,19]
# при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
# при n=10 => 56 * x*10 = 0

# коэффициенты - это числа перед элементами полинома.
# коэффициенты могут быть нулем, кроме первого
# for num1, num2, num3 in zip(koef, : poli = num1 * num2 ** num3
import random

num = int(input('введите число: '))
koef_list = [random.randint(1,100)]
for i in range(num):
    koef_list.append(random.randint(0,100))
list_step = [i for i in range(num,-1,-1)]

#koef_list = [5, 7, 0, 0]

poli = ''
for koef, step in (zip(koef_list, list_step)): #(25, 3)  (15, 2) ... (46, 0)
    if step == 0 and koef != 0:
       string = str(koef) 
    elif step == 1 and koef != 0:
        string = str(koef)+'*x'   
    elif not koef:
       string = ""
    elif koef == 1:
       string = string = 'x**'+str(step)
    else:
        string = string = str(koef)+'*x**'+str(step)
    if string:
        poli += ' + ' + string
poli += ' = 0'
print(poli.strip('+ '))    

poli = ''
for koef, step in (zip(koef_list, list_step)):
    if koef:
        koef = koef if koef > 1 else ''
        poli += str(koef)
        if step:
            poli += '*x'
            if step > 1:
                poli += f'**{str(step)}'
            poli += ' + '
poli += ' = 0'
print(poli)
