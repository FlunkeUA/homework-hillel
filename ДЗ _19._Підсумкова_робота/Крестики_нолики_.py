



# количество клеток
board_size = 3

# игровое поле
board = [1,2,3,4,5,6,7,8,9]

mode_human_vs_human = '1'
mode_human_vs_ai = '2'

def draw_board():
   # Выводим игровое поле

    for i in range(board_size):
        print('', board[i*3], '|',
              board[1+i*3], '|',
              board[2+i*3])
        print('-' * 11)
def game_step(index, char):
    # Функция хода игрока
    if (index > 9 or index < 1 or board[index-1] in ('X', 'O')):
        return False

    board[index - 1] = char
    return True

def check_win(board):
    # Проверяем победу одного из игроков
    win = False

    win_combination = (
        (0,1,2), (3,4,5), (7,8,9), # проверка по горизонтали
        (0,3,6), (1,4,7), (2,5,8),# проверка по вертикали
        (0,4,8), (2,4,6) # проверка по диагонали
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

def computer_step(human, ai):
    # Функционал ИИ

    # найти доступные шаги
    available_steps = [i-1 for i in board if type(i) == int]

    # успешные шаги в приоритете
    win_steps = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    for char in(ai, human):
        for pos in available_steps:
            # клонирование игровой доски
            board_ai = board[:]
            board_ai[pos] = char
            if (check_win(board) != False):
                return pos

   # если мы тут, значит не нашли вариант для победы
    for pos in win_steps:
       if (pos in available_steps):
           return pos
    return False

def next_player(current_player):
    # определяем чей следующий ход
    if (current_player == 'X'):
        return 'O'
    return 'X'

def start_game(mode):
    # текущий игрок
    current_player = 'X'
    ai_player = 'O'
    # номер шага
    step = 1
    draw_board()

    while (step < 10) and (check_win(board) == False):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход):')

        '''ПРОВЕРКА НА ВВОД ЦИФРЫ, НЕ БУКВЫ ИЛИ ЗНАКА'''
        if (index == '0'):
            break

        if (game_step(int(index), current_player)):
            print('Удачный ход')

            current_player = next_player(current_player)

            # увеличим номер хода
            step += 1

            if (mode == '2'):
                ai_step = computer_step('X', 'O')
                # если комп нашел куда ходить
                if (type(ai_step) == int):
                    # ходит комп
                    board[ai_step] = ai_player
                    current_player = next_player(current_player)
                    step += 1

            draw_board()
        else:
            print('Неверный номер')

    if (step == 10):
        print('Игра оконченаю Ничья!')
    elif check_win(board) != False:
        print('Победа! Выиграл: ' + check_win(board))

print('Игра начинается!\n')

mode = 0
while mode not in (mode_human_vs_human, mode_human_vs_ai):
    mode = input('Режим игры:\n1 - Человек против Человека\n2 - Человек против ИИ\nВыберите режим игры:')

start_game(mode)