from random import randint


# создаем игровую доску
def new_board():
    board = []
    for square in range(9):
        board.append(" ")
    return board


# Отображаем игровую доску на экране
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])


# определяем кто будет ходить первый
def first_move():
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


# создаем список доступных ходов
def available_moves(board):
    moves = []
    for square in range(9):
        if board[square] == " ":
            moves.append(square)
    return moves


# алгоритм хода человека
def human_move(board):
    legal = available_moves(board)
    move = None
    while move not in legal:
        move = ask_number("\nТвой ход. Выбери одно из полей (0 - 8):", 0, 9)
        if move not in legal:
            print("\nЭто поле уже занято. Выбери другое.")
    print("Вы выбрали поле №:", move)
    return move

# запрашиваем куда будет ход
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print("Вы ввели не число из диапазона 0-8!!!")
    return response

# алгоритм хода компьютера
def computer_move(board, computer, human):
    # создадим рабочую копию доски,
    # потому что функция будет менять некотороые элементы в списке
    board = board[:]
    # ходы, от лучшего к худшему
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Компьютер выбрал поле №:", end=" ")
    # если сдедующим ходом может победить компьютер, выберем этот ход
    for move in available_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # выполнив проверку этого хода, отменим его (в локальной копии игровой доски)
        board[move] = " "

    # если следующим ходом может победить чегловек, блокируем этот ход
    for move in available_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # выполнив проверку этого хода, отменим его (в локальной копии игровой доски)
        board[move] = " "

    # поскольку следующим ходом ни одна из сторон не может победить,
    # выберем лучшее из доступных полей
    for move in best_moves:
        if move in available_moves(board):
            print(move)
            return move


# алгоритм перехода хода
def next_turn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'


# определяем победителя
def winner(board):
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # по горизонтали
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # по вертикали
        (0, 4, 8), (2, 4, 6)  # по диагонали
    )

    for row in win_combination:
        if board[row[0]] == board[row[1]] == board[row[2]] != " ":
            win = board[row[0]]
            return win
        if " " not in board:
            return "TIE"
    return None

# варианты результатов игры
def congrat_winner(the_winner, computer, human):
    if the_winner != "TIE":
        print("\nТри", the_winner, "в ряд!")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Победа! Выиграл Компьютер!")
    elif the_winner == human:
        print("Победа! Выиграл Человек!")


# предлагаем сыграть заново
def replay():
    replay_game = input("\nЖелаете переиграть? (Y или N)").upper()
    for _ in replay_game:
        if replay_game == "Y" or 'н':
            main()
        else:
            print("Игра закончена!")
            break


# запуск игры
def main():
    computer, human = first_move()
    turn = 'X'
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
    replay()


main()
