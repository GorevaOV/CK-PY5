from random import randint # Подгружаем функцию randit из модуля random

def unique() -> list[int]:
    get_numbers = [randint(-10, 10) for _ in range(15)] # Пишем прочерк, как вы сказали в прошлый раз, а пишем _

    numbers = set(get_numbers)

    while len(numbers) < 15: # Как можно сократить данный цикл, не записывая его в километровую строку?

        numbers = list(numbers)
        numbers.append(randint(-10, 10))
        numbers = set(numbers)

    return list(numbers)


print(unique()) # Результат

