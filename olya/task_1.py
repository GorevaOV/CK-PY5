
from pprint import pprint # подгружаем функцию pprint из модуля pprint
list = []

for symb in range(16):

    b = {'bin': bin(symb), 'dec': symb, 'hex': hex(symb), 'oct': oct(symb)}
    list.append(symb) # Добавляем в список строку полученного словаря

pprint(list)
