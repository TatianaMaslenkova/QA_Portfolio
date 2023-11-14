# Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.
web_list = ['https://github.com/TatianaMaslenkova?tab=repositories', 
            'https://gb.ru/lessons/284811', 
            'https://youtube.com/watch?v=ku-wBaz9uso&list=PLxAJaawE-vksJlT', 
            'https://wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%B', 
            'https://yandex.ru/images/?rdrnd=119335&lr=213&redircnt=1671035434.1', 
            'https://google.com/search?q=colorama+', 
            'https://mixamo.com/#/?page=1&type=Character', 
            'https://dzen.ru/?yredirect=true']
new_list = list(web_list[i].lstrip('https://') for i in range(0, len(web_list)))
print(list(map(lambda i: i[:i.find('/')], new_list)))
# убираем лишнее из начала строки с помощью функции lstrip()
# печатаем список доменных имён сайтов (символы от нулевого до '/')