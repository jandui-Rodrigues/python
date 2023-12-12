"""
Varias jogadas com um dado de 6 lados

Voce deve combinar as jogadas que somam 7
Descubra as duplas possiveis de se formar
Cada jogada pode ser usada apenas uma vez
"""


def get_seven(rolls):
    sean_before = set()
    lucky_rolls = list()

    for roll in rolls:
        if 7 - roll in sean_before:
            lucky_rolls.append((7 - roll, roll))
            sean_before.discard(7 - roll)
        else:
            sean_before.add(roll)
    return lucky_rolls


if __name__ == "__main__":
    rolls = [5, 2, 6, 3, 4, 6, 3, 1, 6, 1]
    # resultado esperado: [(5, 2), (6, 1), (6, 1), (4, 3)]
    print(get_seven(rolls))
