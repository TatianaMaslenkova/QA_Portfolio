# Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]
import random
size = 200
init_list = [random.randint(1, 100) for _ in range(0, size)]
print(init_list)
new_list = [(index, init_list[index]) for index in range(0, size) if (index+init_list[index]) % 5 == 0]
print(f'Список кортежей:\n{new_list}\n')

# если через filter:
# import random
# size = 200
# init_list = [random.randint(1, 100) for _ in range(0, size)]
# print(init_list)
# new_list = list(filter(lambda i: (i[0]+i[1]) % 5 == 0, enumerate(init_list)))
# print(f'Список кортежей:\n{new_list}\n')