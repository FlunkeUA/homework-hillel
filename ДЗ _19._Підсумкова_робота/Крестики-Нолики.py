class Board:
    def __init__(self, field_demension=15):
        self.field_demension = field_demension

        self.field =[]
        for _ in range(field_demension):
            self.field.append([None] * field_demension)

        self.next_move = "X"
        self.result = None
        self.game_is_over = False
        self.last_move_coordinates = None

    def is_coords_inside(self, coords):
        return (
                0 <= coords[0] < self.field_demension
                and 0 <= coords[1] < self.field_demension
        )

    def check_if_game_is_over(self):
        if self.last_move_coordinates is None:
            return

        in_a_raw_to_win = 5 if self.field_demension >= 5 else 3

        symbol_to_check = self.field[self.last_move_coordinates[0]][self.last_move_coordinates[1]]

        currently_in_a_raw = 0
        for coordinates_to_change in ((0, ), (1, ), (0,1)):
            coordinates_to_check = list(self.last_move_coordinates)
        for i in range(-in_a_raw_to_win + 1, in_a_raw_to_win):
            for single_coordinate in coordinates_to_change:
                coordinates_to_check[single_coordinate] += i

            raw_to_check, col_to_check = coordinates_to_check

            if not self.is_coords_inside(raw_to_check, col_to_check):
                return

            if self.field[raw_to_check][col_to_check] == symbol_to_check:
                currently_in_a_raw += 1
            else:
                currently_in_a_raw = 0

            if currently_in_a_raw == in_a_raw_to_win:
                self.game_is_over = True
                self.result = f'Winner: {symbol_to_check}'

class View:
    def draw_board(self, board):
        for row in board.field:
            for cell in row:
                print((cell or " "), end="|")

            print()
            print("--" * board.field_demension)

    def print_message(self, message):
        print(message)

class Controller:
    def __init__(self, view, board):
        self.view = view
        self.board = board

    def place_move(self, position: tuple):
        self.board.field[position[0]][position[1]] = self.board.next_move
        self.board.next_move = 'X' if self.board.next_move == '0' else '0'
        self.board.last_move_coordinates = position

    def get_next_move(self):
        self.view.print_message(f'Input place where you want to move: {self.board.next_move}')

        inputted_raw, inputted_colum = None, None
        while True:
            inputed_coordinates = input()
            try:
                inputted_raw, inputted_colum = inputed_coordinates.split(',')
                inputted_raw = int(inputted_raw)
                inputted_colum = int(inputted_colum)
            except Exception:
                self.view.print_message('Input coordinates in format raw,colum')
                continue

            if not self.board.is_coords_inside(inputted_raw, inputted_colum):
                self.view.print_message('Coordinates must bee in field size')
                continue

            if self.board.field[inputted_raw][inputted_colum] is not None:
                self.view.print_message('This place is used already')
                continue

            break

        return inputted_raw, inputted_colum

    def start_game(self):
        self.view.print_message('Game Start')
        while not self.board.game_is_over:
            self.view.draw_board(self.board)
            next_move = self.get_next_move()
            self.place_move(next_move)
            self.board.check_if_game_is_over()

        self.view.print_message(f'Result - {self.board.result}')

if __name__ == '__main__':
    controller = Controller(View(), Board(3))
    while True:
        controller.start_game()
        play_again = input('Play again?')
        if not play_again or play_again.lower() in ['no', 'n', 'ні']:
            break

















