from random import randint

# глобальные константы
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def ask_number(question, low, high):
    """Просим ввести число из диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Определяем принадлежность перового хода."""
    go_first = randint(0, 1)
    if go_first == 1:
        print("\nПервым ходит Человек!")
        human = 'X'
        computer = 'O'
    else:
        print("\nПервым ходит Компьютер!")
        computer = 'X'
        human = 'O'
    return computer, human

def new_board():
    """Создаём новую игровую доску."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Отображаем игровую доску на экране."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])


def legal_moves(board):
    """Создаём список доступных ходов."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Определяем победителя в игре."""
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # по горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # по вертикали
        (0, 4, 8), (2, 4, 6)  # по диагонали
    )

    for row in win_combination:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("\nТвой ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nЭто поле уже занято. Выбери другое.\n")
    print("Вы выбрали поле №:", move)
    return move


def computer_move(board, computer, human):
    """Определяем ход за компьютер."""
    # создадим рабочую копию доски, потому что функция будет менять некотороые элементы в списке
    board = board[:]
    # ходы, от лучшего к худшему
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Компьютер выбрал поле №:", end=" ")
    # если сдедующим ходом может победить компьютер, выберем этот ход
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # выполнив проверку этого хода, отменим его (в локальной копии игровой доски)
        board[move] = EMPTY

    # если следующим ходом может победить чегловек, блокируем этот ход
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # выполнив проверку этого хода, отменим его (в локальной копии игровой доски)
        board[move] = EMPTY

    # поскольку следующим ходом ни одна из сторон не может победить,
    # выберем лучшее из доступных полей
    for move in best_moves:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Осуществляет переход хода."""
    if turn == 'X':
        return 'O'
    else:
        return 'X'

def congrat_winner(the_winner, computer, human):
    """Поздравляем победителя игры."""
    if the_winner != TIE:
        print("\nТри", the_winner, "в ряд!")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победа! Выиграл Компьютер!")
    elif the_winner == human:
        print("Победа! Выиграл Человек!")

def replay():
    """Предлагаем сыграть заново"""
    replay_game = input("\nЖелаете переиграть? (Y или N)").upper()
    for _ in replay_game:
        if replay_game == "Y":
            main()
        else:
            print("Игра закончена!")
            break


def main():
    computer, human = pieces()
    turn = 'X'
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
    replay()

# запуск программы
main()
