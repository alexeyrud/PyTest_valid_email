"""
Написать функцию, которая принимает имя файла, открывает файл (предполагается, что это html),
заменяет все email адреса на user@example.com и сохраняет результат в файл, с таким же именем, как исходный,
но с добавлением суффикса '.processed'
"""
import re

INPUT_FILE    = 'inp.htm'
EMAIL_REPLACE = 'user@example.com'

"""
Взят произвольный файл со списком email (http://www.mevriz.ru/images/list_avtor.doc), cконвертирован в htm с помощью
MS-Word для того чтоб получить максимально "сложный" для парсинга файл
"""

# ======= start function for replacing e-mail =========
def repl_email(input_file):
    output_file = input_file + '.processed'

    email_re = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*")'  # quoted-string
        r'@((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+)(?:[A-Z0-9-]{2,63}(?<!-))',  # domain
        re.IGNORECASE)
    """
    Регулярное выражение валидации e-mail взято из jango
    https://github.com/django/django/blob/master/django/core/validators.py
    По-хорошему лучше подключить
    from django.core import validators
    и использовать валидаторы оттуда.
    Но в таком случае есть смысл использовать сторонние библиотеки и для парсинга html
    """

    tag_re = re.compile('<|>| |\b|\)|\(|:|\t|\"|\||;|,')
    """
    Шаблон для разбора строки на "атомы" для передачи валидатору е-мейла Перечислены возможные "разделители" для
    split
    """

    with open(input_file) as inputFile:
        with open(output_file, 'w') as outputFile:
            for str in inputFile:                   # Читаем файл построчно
                str_res = str                       # Сохраняем исходную строку
                for str_tmp in tag_re.split(str):   # разбиваем полученную строку возможными "разделителями"
                    if email_re.match(str_tmp):     # валидируем части кортежа джанговской регуляркой
                        str_res = str_res.replace(str_tmp, EMAIL_REPLACE, 1)  # При совпадении меняем e-mail
                outputFile.write(str_res)           # записываем результирующую строку
        outputFile.close()
    inputFile.close()


# =========== main ==================================

repl_email(INPUT_FILE)

# ======== end main =================================
