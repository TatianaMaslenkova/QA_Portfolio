# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов 
# влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно 
# зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования. Ваша задача - написать функцию, которая записывает в файл 
# шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


def encrypt_text(alpha: str, txt: str, k: int) -> str:
    '''
    Возвращает зашифрованную строку

        Args:
            alpha (str) - алфавит
            txt (str) - строка, которую нужно зашифровать
            k (int) - ключ шифрования (количество символов смещения)
        Returns:
            encrypted_text (str) - зашифрованная строка
    '''
    encrypted_text = ''
    for symbol in txt:
        i = 0
        for char in alpha:
            if symbol == char:
                index = i + k
            i += 1
        if index > len(alpha):
            index = (index+k) % len(alpha) # по аналогии с игрой с монетками (если ведущий называет число, превышающее кол-во игроков)
        encrypted_text += alpha[index]
    return encrypted_text

def decrypt_text(alpha: str, txt: str, k: int) -> str:
    '''
    Возвращает расшифрованную строку

        Args:
            alpha (str) - алфавит
            txt (str) - строка, которую нужно расшифровать
            k (int) - ключ шифрования (количество символов смещения)
        Returns:
            encrypted_text (str) - зашифрованная строка
    '''
    decrypted_text = ''
    for symbol in txt:
        i = 0
        for char in alpha:
            if symbol == char:
                index = i - k
            i += 1
        if index < 0:
            index = len(alpha) + index
        if index >= len(alpha):
            index -= len(alpha)
        decrypted_text += alpha[index]
    return decrypted_text

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя !"№;%:?*()-_+='
text = 'Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.'
key1 = int(input("Введите ключ шифрования: "))
encrypted_text = encrypt_text(alphabet, text, key1)
with open('Caesar_en.txt', 'w', encoding='UTF8') as write_file:
    write_file.write(encrypted_text)
with open('Caesar_en.txt', 'r', encoding='UTF8') as read_file:
    read_file.read()
print('Текст зашифрован в файле "Caesar_en.txt"')

key2 = int(input("Введите ключ дешифрования: "))
with open('Caesar_en.txt', 'r', encoding='UTF8') as r_file:
    r_file.read()
decrypted_text = decrypt_text(alphabet, encrypted_text, key2)
with open('Caesar_decr.txt', 'w', encoding='UTF8') as w_file:
    w_file.write(decrypted_text)
print('Текст расшифрован в файле "Caesar_decr.txt"')