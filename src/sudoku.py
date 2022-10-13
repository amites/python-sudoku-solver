import copy


class SudokuMethods:
    """
    Utility methods for Sudoku puzzles.
    """

    def __init__(self):
        self.attempts = 0
        self.board = None
        self.board_original = None

    @staticmethod
    def parse_str(board_str):
        clean_str = board_str.replace('\n', '').replace(' ', '').replace('\n', '')
        return [[int(s) if s.isnumeric() else 0 for s in clean_str[idx:idx + 9]]
                for idx in range(0, len(clean_str), 9)]

    def set_board(self, board):
        if type(board) == str:
            board = self.parse_str(board)
        self.board = board
        self.board_original = copy.deepcopy(board)
        return board

    def format_str(self, **kwargs):
        board = kwargs.get('board', self.board)
        if not board:
            print('ERROR: Board not loaded, cannot parse')
            return ''
        placeholder = kwargs.get('placeholder', '0')

        def _val(v):
            return str(v) if placeholder == '0' else str(v).replace('0', placeholder)

        method = kwargs.get('method', 'single')
        if method == 'single':
            join_char = ' ' if kwargs.get('spaces', True) else ''
            return join_char.join([''.join(''.join(str(_val(n))) for n in b) for b in board])
        elif method == 'multi':
            bar = '─────────────────────'
            output = []

            for b in range(9):
                if b > 0 and b % 3 == 0:
                    output.append(bar)
                row = []
                for n in range(9):
                    if 9 > n > 0 == n % 3:
                        row.append('┃')
                    row.append(_val(board[b][n]))
                output.append(' '.join(row))
            return '\n'.join(output)
        else:
            print('ERROR: method "{}" not supported'.format(method))
            return ''

    @staticmethod
    def is_valid_board(board):
        for i in range(9):
            valid_row = SudokuMethods._valid_group(board[i])
            valid_col = SudokuMethods._valid_group([row[i] for row in board])

            if not valid_row or not valid_col:
                return False

        return bool(SudokuMethods._valid_squares(board))

    @staticmethod
    def _valid_group(_group):
        group = list(filter(lambda a: a != 0, _group))
        if any(0 > i > 9 for i in group):
            return False
        return bool(len(group) == len(set(group)))

    @staticmethod
    def _valid_squares(board):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                group = []
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] != 0:
                            group.append(board[r][c])
                if not SudokuMethods._valid_group(group):
                    return False
        return True

    def solve_board(self, board):
        self.set_board(board)
        self.attempts = 0

        self._solve()

        return self.board

    def _solve(self):
        def find_empty():
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j] == 0:
                        return i, j  # row, column
            return None

        find = find_empty()
        if not find:
            return True
        row, col = find

        for num in range(1, 10):
            if self._is_valid_num_position(num, (row, col)):
                self.board[row][col] = num

                # exit when all results are valid
                if self._solve():
                    return True
                # invalid result -- reset to 0 and try again
                self.board[row][col] = 0
        # not solved yet, keep  trying
        return False

    def _is_valid_num_position(self, num, position):
        # row check
        for i in range(len(self.board[0])):
            if self.board[position[0]][i] == num and position[1] != i:
                return False

        # column check
        for i in range(len(self.board)):
            if self.board[i][position[1]] == num and position[0] != i:
                return False

        # box check
        box_x = position[1] // 3
        box_y = position[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != position:
                    return False
        return True


if __name__ == '__main__':
    print('\n\n#### SUDOKU ####\n')

    # valid puzzle
    sudoku = SudokuMethods()
    example_puzzle_a = '..3..5..1 2..3...4. 1....7..5 ......... ......... .02..6... ......... 81....... .........'

    print('Original puzzle A:\n\t{}\n'.format(sudoku.board_original))
    sudoku.solve_board(example_puzzle_a)
    print('Solved puzzle A:\n\t{}\n\n'.format(sudoku.board))

    example_puzzle_b = '5.7...8.. .6...9... 9....4... .4..8.7.1 .1....5.. ...7....3 9.6.1.... .5....3.. 4......2.'
    print('Original puzzle B:\n\t{}\n'.format(sudoku.board_original))
    sudoku.solve_board(example_puzzle_b)
    print('Solved puzzle B:\n\t{}\n\n'.format(sudoku.board))
