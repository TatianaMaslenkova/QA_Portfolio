# Создайте программу для игры в ""Крестики-нолики""
from typing import List
def print_field(field: List[int]) -> List[int]:
    '''
    Печатает игровое поле

        Args:
            field (List[int]) - список с количеством ячеек
        Returns:
            field (List[int]) - напечатанный список в виде игрового поля
    '''
    print('-'*13)
    for i in range(3):
        print('|', field[0+i*3],'|', field[1+i*3], '|', field[2+i*3], '|')
        print('-'*13)

def choice(char: str) -> str:
    '''
    Просит игрока, который ходит, выбрать ячейку, в которую поставить его игровой знак, проверяет введённые данные, и ставит знак игрока и передаёт ход другому игроку, если проверка пройдена, если нет - просит повторно ввести номер ячейки.

        Args:
            char (str) - Х или 0
        Returns:
            char (str) - Х или 0
    '''
    order = False
    while not order:
        cell_number = input(f'Игрок, который ходит {char}, выберите ячейку: ')
        try:
            cell_number =int(cell_number)
        except:
            print('Такой ячейки нет. Попробуйте ещё раз')
            continue
        if 1 <= cell_number <= 9:
            if(str(field[cell_number-1]) not in 'X0'):
                field[cell_number-1] = char
                order = True
            else:
                print('Эта ячейка занята')
        else:
            print('Такой ячейки нет. Попробуйте ещё раз')

def victory_check(field: list) -> str:
    '''
    Проверяет выигрыш игроков
        Args:
            field (list) - игровое поле
        Returns:
            field[i[0]] (str) - Х или 0
    '''
    victory = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in victory:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False

def game(field):
    '''
    Проводит игру двух игроков в крестики-нолики
        Args:
            field (list) - игровое поле
        Returns:
            str - строка с результатами игры
    '''
    print('Добро пожаловать в игру в крестики нолики!')
    count = 0
    victory = False
    while victory == False:
        print_field(field)
        if count % 2 != 0:
            choice('0')
        else:
            choice('X')
        count +=1
        if count > 4:
            winner = victory_check(field)
            if winner:
                print(f'Победил игрок, ходивший {winner}')
                victory = True
                print_field(field)
                break
            if count == 9:
                print('Ничья')
                print_field(field)
                break   

field = list(range(1,10))
game(field)