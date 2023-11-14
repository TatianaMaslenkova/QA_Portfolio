# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021(или сколько вы 
# скажете) конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход 
# можно забрать не более чем 28(или сколько вы зададите в начале) конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сделайте эту игру. a) Добавьте игру против бота. b) Подумайте как наделить бота ""интеллектом""
# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом, лучше выделите в отдельные 
# функции бота и умного бота.
import random
def game_choice(player: int) -> str:
    '''
    Возвращает выбор режима игры/введённое имя игрока

        Args:
            player (int) - номер игрока
        Returns:
            player (str) - строка с именем игрока
    '''
    player = input('Введите имя игрока или введите "Bot" для игры с ботом или "iBot" для игры с умным ботом: ')
    if player != 'Bot' and player != 'iBot':
        return player
    elif player == 'Bot':
        return f'Bot'
    else: 
        return f'iBot'

def start_game(curr_am: int, lim: int) -> int:
    '''
    Возвращает результат жеребьёвки

        Args:
            curr_am (int) - текущее кол-во конфет
            lim (int) - максимальное количество конфет, которое можно взять за один ход
        Returns:
            int - номер игрока, который ходит первым
    '''
    print(f'На столе {curr_am} конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. Брать можно от 1 до {lim} конфет. Все конфеты оппонента достаются сделавшему последний ход.')
    draw = random.randint(0, 1) # жеребьёвка
    if draw == 0:
        return 0
    else:
        return 1


def limit_check(num: int, lim: int) -> int:
    '''
    Проверяет кол-во конфет, которые берёт игрок, и возвращает его, если не превышен лимит

        Args:
            num (int) - кол-во конфет, которое ввёл игрок
            lim (int) - максимальное количество конфет, которое можно взять за один ход
        Returns:
            num (int) - кол-во конфет, которое ввёл игрок
    '''
    while True:
        try:
            num = int(num)
        except ValueError:
            num = input('Нужно ввести число. Повторите ввод: ')
        else:
            if num > lim or num < 1:
                num = input(f'Брать меньше 1 или больше {lim} нельзя! Введите другое число: ')
            else:
                break
    return num

def p_print(pl: str, num: int, count: int, curr_am: int) -> str:
    '''
    Печатает действие ходившего игрока и текущую ситуацию

        Args:
            pl (str) - имя ходившего игрока
            num (int) - кол-во конфет, которое он взял со стола
            count (int) - кол-во конфет у игрока после хода
            curr_am (int) - текущее кол-во конфет
        Returns:
            str - строка с описанием действий игрока текущей ситуации
    '''
    print(f"Ходил {pl}, он взял {num} конфет, теперь у него {count}. На столе осталось {curr_am} конфет.")

def p2p_game(curr_am: int, lim: int, pl1: str, pl2: str, draw: int) -> str:  # 2 игрока
    '''
    Проводит игру двух игроков и возвращает победителя

        Args:
            curr_am (int) - текущее кол-во конфет
            lim (int) - максимальное количество конфет, которое можно взять за один ход
            pl1 (str) - имя первого игрока
            pl2 (str) - имя второго игрока
            draw (int) - результат жеребьёвки
        Returns:
            str - строка с именем победителя
    '''
    count1 = 0 # конфеты первого игрока
    count2 = 0 # конфеты второго игрока

    while curr_am > lim:
        if draw == 0:
            num1 = limit_check(input(f'{pl1}, сколько конфет хотите взять? '), lim)
            count1 += num1
            curr_am -= num1
            p_print(pl1, num1, count1, curr_am)
            draw = True
            if 0 < curr_am <= lim:
                print(f'Выиграл {pl2}')
        else:
            num2 = limit_check(input(f'{pl2}, сколько конфет хотите взять? '), lim)
            count2 += num2
            curr_am -= num2
            p_print(pl2, num2, count2, curr_am)
            draw = False
            if 0 < curr_am <= lim:
                print(f'Выиграл {pl1}')

def p2bot_game(curr_am: int, lim: int, pl1: str, pl2: str, draw: int): # игра человек против бота
    '''
    Проводит игру человека против бота и возвращает победителя

        Args:
            curr_am (int) - текущее кол-во конфет
            lim (int) - максимальное количество конфет, которое можно взять за один ход
            pl1 (str) - имя первого игрока
            pl2 (str) - имя второго игрока
            draw (int) - результат жеребьёвки
        Returns:
            str - строка с именем победителя
    '''
    count1 = 0 # конфеты первого игрока
    count2 = 0 # конфеты второго игрока

    while curr_am > lim:
        if pl1 != 'Bot' and pl1 != 'iBot': # если 1-й игрок - человек
            if pl2 == 'Bot':  # если 2-й игрок - бот
                if draw == 0: # если 1-й игрок - человек ходит первым
                    num = limit_check(input(f'{pl1}, сколько конфет хотите взять? '), lim)
                    count1 += num
                    curr_am -= num
                    p_print(pl1, num, count1, curr_am)
                    draw = True
                    if 0 < curr_am <= lim:
                        print(f'Выиграл {pl2}')
                else: # если 2-й игрок - бот ходит вторым
                    num = random.randint(1,lim)
                    count2 += num
                    curr_am -= num
                    p_print(pl2, num, count2, curr_am)
                    draw = False
                    if 0 < curr_am <= lim:
                        print(f'Выиграл {pl1}')
        else: # если 2-й игрок - человек
            if pl1 == 'Bot':  # если 1-й игрок - бот
                if draw == 0: # если 1-й игрок - бот ходит первым
                    num = random.randint(1,lim)
                    count1 += num
                    curr_am -= num
                    p_print(pl1, num, count1, curr_am)
                    draw = True
                    if 0 < curr_am <= lim:
                        print(f'Выиграл {pl2}')
                else: # если 2-й игрок - человек ходит вторым
                    num = limit_check(input(f'{pl2}, сколько конфет хотите взять? '), lim)
                    count2 += num
                    curr_am -= num
                    p_print(pl2, num, count2, curr_am)
                    draw = False
                    if 0 < curr_am <= lim:
                        print(f'Выиграл {pl1}')
                
def p2ibot_game(curr_am: int, lim: int, pl1: str, pl2: str, draw: int): # игра человек против умного бота
    '''
    Проводит игру человека против умного бота и возвращает победителя

        Args:
            curr_am (int) - текущее кол-во конфет
            lim (int) - максимальное количество конфет, которое можно взять за один ход
            pl1 (str) - имя первого игрока
            pl2 (str) - имя второго игрока
            draw (int) - результат жеребьёвки
        Returns:
            str - строка с именем победителя
    '''
    count1 = 0 # конфеты первого игрока
    count2 = 0 # конфеты второго игрока

    while curr_am > lim:
        if pl1 != 'iBot' and pl1 != 'iBot': # если 1-й игрок - человек
            if pl2 == 'iBot':  # если 2-й игрок - умный бот
                if draw == 0: # если 1-й игрок - человек ходит первым
                    num = limit_check(input(f'{pl1}, сколько конфет хотите взять? '), lim)
                    count1 += num
                    curr_am -= num
                    p_print(pl1, num, count1, curr_am)
                    draw = True
                    if 0 < curr_am <= lim:
                        print(f'Выиграл {pl2}')
                else: # если 2-й игрок - бот ходит вторым
                    if curr_am % (lim + 1) != 0:
                        num = curr_am % (lim + 1)
                    else:
                        num = random.randint(1,lim)
                    count2 += num
                    curr_am -= num
                    p_print(pl2, num, count2, curr_am)
                    draw = False
                    if 0 < curr_am <= lim:
                        print(f'Выиграл {pl1}')
        elif pl2 != 'iBot' and pl2 != 'iBot': # если 2-й игрок - человек
            if pl1 == 'iBot':  # если 1-й игрок - бот
                if draw == 0: # если 1-й игрок - бот ходит первым
                    if curr_am % (lim + 1) != 0:
                        num = curr_am % (lim + 1)
                    else:
                        num = random.randint(1,lim)
                    count1 += num
                    curr_am -= num
                    p_print(pl1, num, count1, curr_am)
                    draw = True
                    if 0 < curr_am <= lim:
                        print(f'Выиграл {pl2}')
                else: # если 2-й игрок - человек ходит вторым
                    num = limit_check(input(f'{pl2}, сколько конфет хотите взять? '), lim)
                    count2 += num
                    curr_am -= num
                    p_print(pl2, num, count2, curr_am)
                    draw = False
                    if 0 < curr_am <= lim:
                        print(f'Выиграл {pl1}')                    
            
initial_amount = abs(int(input('Введите с каким количеством конфет хотите начать игру: ')))
limit = abs(int(input('Определите максимальное количество конфет, которое можно взять за один ход: ')))
player1 = game_choice(1)
player2 = game_choice(2)
draw = start_game(initial_amount, limit)
if draw == 0:
    print(f'По результатам жеребьёвки, первым ходит {player1}')
else:
    print(f'По результатам жеребьёвки, первым ходит {player2}')
    
if player1 != 'Bot' and player1 != 'iBot': # если первый - человек
    if player2 != 'Bot' and player2 != 'iBot': # если второй - человек
        p2p_game(initial_amount, limit, player1, player2, draw)
    elif player2 == 'Bot': # если второй - бот
        p2bot_game(initial_amount, limit, player1, player2, draw)
    elif player2 == 'iBot': # если второй - умный бот
        p2ibot_game(initial_amount, limit, player1, player2, draw)
else: # если второй - человек
    if player1 == 'Bot': # если первый - бот
        p2bot_game(initial_amount, limit, player1, player2, draw)
    elif player1 == 'iBot': # если первый - умный бот
        p2ibot_game(initial_amount, limit, player1, player2, draw)