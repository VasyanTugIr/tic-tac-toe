# ┌───┬───┬───┐
# │   │   │   │
# ├───┼───┼───┤
# │   │   │   │
# ├───┼───┼───┤
# │   │   │   │
# └───┴───┴───┘
from os import system
from random import choice


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

    KR1 -= 1
    KR2 -= 1
    res = KR1 * 3 + KR2

    if res not in available:
        raise Exception("Это поле уже занято. Попробуй еще раз!")
    return res


def computer_move(Avaible):
    if len(Avaible) != 0:
        return choice(Avaible)


def check_game_over(available, field):
    winner = find_game_over(field)
    if winner != None:
        system("cls")
        draw_field(field)
        print(f"Победили {winner}")
        return True
    elif len(available) == 0:
        system("cls")
        draw_field(field)
        print("Ничья")
        return True
    else:
        return False


def find_game_over(field):

    win_lst = [
        [field[0], field[1], field[2]],
        [field[3], field[4], field[5]],
        [field[6], field[7], field[8]],
        [field[0], field[3], field[6]],
        [field[1], field[4], field[7]],
        [field[2], field[5], field[8]],
        [field[0], field[4], field[8]],
        [field[2], field[4], field[6]],
    ]
    for lst in win_lst:
        if lst[0] != " ":
            if lst[0] == lst[1] == lst[2]:
                return lst[0]
    else:
        return None


available = [i for i in range(9)]
lst = [" "] * 9
game_over = False
print("Как вы хотите играть?")
print(
    """
1.Друг
2.Компьютер
"""
)
game_type = int(input())


while not game_over:
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
        draw_field(lst)
        game_over = check_game_over(available, lst)
        if not game_over:
            if game_type == 1:
                error = True
                while error:
                    try:
                        move = human_move(available)
                        error = False
                    except Exception as e:
                        print(e)
                        system("pause")
            elif game_type == 2:
                move = computer_move(available)
            lst[move] = "O"
            available.remove(move)
            game_over = check_game_over(available, lst)
