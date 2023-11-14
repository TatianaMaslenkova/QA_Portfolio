# По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. При этом каждый из
# тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты. Далее
# человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам
# выбывает из круга. Процесс продолжается с места остановки аналогичным образом до последнего человека
# в круге. Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, то импортируйте
# библиотеку time и используйте оттуда функцию sleep. Определите номер этого человека и количество
# монет, которые оказались у него в конце игры.

def anounced_num_check(num, counter):
    if num > counter:
        new_num = num % counter
        return new_num
    return num

def players_coins_state(players, coins):
    print(f'Игроков в игре: {players}\nМонет у игроков: {coins}')

def res_of_count(players, coins, counter):
    for i in range(0, len(players)):
        if i < counter:
            coins[i] += 1
        else:
            coins[i] += 2
    print('Игроки получили монеты')
    return coins

n_of_players = abs(int(input('Введите количество игроков:\n')))
list_of_players = []
list_of_coins = []

for i in range(0, n_of_players):
    list_of_players.append(i)
    list_of_coins.append(0)

for i in range(0, len(list_of_players)):
    players_coins_state(list_of_players, list_of_coins)

    anounced_number = abs(int(input('Ведущий объявляет номер:\n')))
    count = anounced_num_check(anounced_number, n_of_players)
    print(count)

    res_of_count(list_of_players, list_of_coins, count)
    players_coins_state(list_of_players, list_of_coins)

    last_player = count
    if (count == len(list_of_players)):
        last_player = 0

    print(f'Игроку {list_of_players[count-1]} сегодня не везет.\n{list_of_coins[count-1]} монет достаются игроку {list_of_players[last_player]}')

    if (count == len(list_of_players)):
        change = list_of_coins.pop(count-1) + list_of_coins.pop(last_player)
        list_of_coins.insert(0, change)
        list_of_players.pop(count-1)
    else:
        change = list_of_coins.pop(last_player-1) + list_of_coins.pop(count-1)
        list_of_coins.insert(last_player-1, change)
        list_of_players.pop(count-1)

    players_coins_state(list_of_players, list_of_coins)

    list_players = list_of_players[:]
    while count < len(list_players)+1:
        list_players.pop(count-1)
    
    list_coins = list_of_coins[:]
    while count < len(list_coins)+1:
        list_coins.pop(count-1)

    print(f'Следующий круг: ')
    players_coins_state(list_of_players[count-1:] + list_players, list_of_coins[count-1:] + list_coins)

    list_of_players = list_of_players[count-1:] + list_players
    list_of_coins = list_of_coins[count-1:] + list_coins

    if (len(list_of_players) > 1):
        quit = input(
            'Хотите продолжить или выйти из игры?\n Q - выйти:  ')
        if (quit == 'Q' or quit == 'q'):
            print('Жаль, что покидаете игру, не доиграв до конца.')
            break
    else:
        print(f'Победил игрок {list_of_players}, заработав {list_of_coins} монет')
        break

