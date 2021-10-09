# ┌───┬───┬───┐
# │   │   │   │
# ├───┼───┼───┤
# │   │   │   │
# ├───┼───┼───┤
# │   │   │   │
# └───┴───┴───┘
from os import system


def draw_field(Field):
    print(
        f"""
       1   2   3
     ┌───┬───┬───┐    
  1  │ {Field[0]} │ {Field[1]} │ {Field[2]} │
     ├───┼───┼───┤
  2  │ {Field[3]} │ {Field[4]} │ {Field[5]} │
     ├───┼───┼───┤
  3  │ {Field[6]} │ {Field[7]} │ {Field[8]} │
     └───┴───┴───┘  
"""
    )


def human_move(available):
    print("Введите координаты")
    try:
        KR1 = int(input())
        KR2 = int(input())
    except ValueError:
        raise ValueError("Буквы не цифры!Переделай.")
    if KR1 > 3 or KR1 < 1 or KR2 > 3 or KR2 < 1:
        raise ValueError("Ты ввел не существующие координаты. Переделай.")

    # 0 1 2
    # 3 4 5
    # 6 7 8

    # 1 3 = 0*3 + 2-> 2
    # 3 3 = 2*3 + 2-> 8
    if KR1 == 1 and KR2 == 1:
        if 0 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 0

    if KR1 == 1 and KR2 == 2:
        if 1 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 1

    if KR1 == 1 and KR2 == 3:
        if 2 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 2

    if KR1 == 2 and KR2 == 1:
        if 3 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 3

    if KR1 == 2 and KR2 == 2:
        if 4 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 4

    if KR1 == 2 and KR2 == 3:
        if 5 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 5

    if KR1 == 3 and KR2 == 1:
        if 6 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 6

    if KR1 == 3 and KR2 == 2:
        if 7 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 7

    if KR1 == 3 and KR2 == 3:
        if 8 not in available:
            raise Exception("Это поле уже занято. Попробуй еще раз!")
        return 8


available = [i for i in range(9)]
lst = [" "] * 9

while True:
    system("cls")
    draw_field(lst)
    try:
        move = human_move(available)
    except Exception as e:
        print(e)
        system("pause")
    else:
        lst[move] = "X"
        available.remove(move)
