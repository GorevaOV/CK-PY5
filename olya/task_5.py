from random import sample # Подгружаем функцию sample из модуля random

def password(n=8) -> str:

    baza_4isel = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ' # Источник

    return "".join(sample(baza_4isel, n))

print(password())
# На деле нужно ввести, условие, чтобы в пароле обязательно содержал цифры, но как это сделать я не знаю