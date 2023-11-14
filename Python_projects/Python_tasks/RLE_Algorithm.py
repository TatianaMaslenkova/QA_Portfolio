# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные
# хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл

def rle_encrypt_text() -> str:
    '''
    Возвращает сжатую строку

        Args:
            txt (str) - строка, которую нужно сжать
        Returns:
            compressed_txt (str) - сжатая строка
    '''
    with open('Task5_init_text.txt', 'r', encoding='UTF8') as read_file:
        rle_text = read_file.read()
    index = 0
    count = 1
    compressed_txt = ''
    rle_text += ' '
    while index < len(rle_text)-1:
        if rle_text[index] == rle_text[index + 1]:
            count += 1
            index += 1
        elif rle_text[index] != rle_text[index + 1]:
            if count == 1:
                compressed_txt += rle_text[index]
                index += 1
            else:
                compressed_txt += str(count) + rle_text[index]
                count = 1
                index += 1
        elif rle_text[index] == -1:
            compressed_txt += rle_text[index]
    with open('Task5_compressed_text.txt', 'w', encoding='UTF8') as w_file:
        w_file.write(compressed_txt)
    return compressed_txt

def decrypt_text() -> str:
    '''
    Распаковывает сжатую строку

        Args:
            txt (str) - строка, которую нужно распаковать
        Returns:
            decompressed_txt (str) - распакованная строка
    '''
    with open('Task5_compressed_text.txt', 'r', encoding='UTF8') as read_file:
        text_to_decompress = read_file.read()
    index = 0
    count = ''
    decompressed_txt = ''
    while index < len(text_to_decompress):
        if text_to_decompress[index].isdigit():
            count += text_to_decompress[index]
            index += 1
        elif count == '':
            decompressed_txt += text_to_decompress[index]
            index += 1
        else:
            decompressed_txt += text_to_decompress[index] * int(count)
            count = ''
            index += 1
    return decompressed_txt

text = 'AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
with open('Task5_init_text.txt', 'w', encoding='UTF8') as write_file:
    write_file.write(text)
compressed_txt = rle_encrypt_text()
print(compressed_txt)
decompressed_txt = decrypt_text()
print(decompressed_txt)

