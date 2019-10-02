"""
В Python 3 существуют так называемые подгенераторы (subgenerators).
Если в функции-генераторе встречается пара ключевых слов yield from,
после которых следует объект-генератор, то данный генератор делегирует
доступ к подгенератору, пока он не завершится (не закончатся его значения),
после чего продолжает своё исполнение.
"""


def generator():
    yield from (3 * x for x in range(5))
    yield from (2 * x for x in range(5, 10))


for i in generator():
    print(i)


# def generator():
#     yield from range(10)
#     yield 'end'

# for value in generator():
#     print(value)

