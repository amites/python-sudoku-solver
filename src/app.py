from flask import Flask, request

from sudoku import SudokuMethods


app = Flask(__name__)


@app.route('/solve', methods=['POST'])
def solve_puzzle():
    board_string = request.form['board']
    # TODO: add string validation for user input
    try:
        board = SudokuMethods.parse_str(board_string)
        is_valid = SudokuMethods.is_valid_board(board)
        if not is_valid:
            return 'Invalid', 406
        sudoku = SudokuMethods()
        result = sudoku.solve_board(board)
        if result:
            return sudoku.format_str(), 202
        return 'Invalid', 422
    except AttributeError:
        return 'Invalid Request', 400
    except (Exception,):
        return 'Unknown Error', 500


@app.route('/validate', methods=['POST'])
def validate_puzzle():
    board_string = request.form['board']
    try:
        # TODO: add string validation for user input
        board = SudokuMethods.parse_str(board_string)
        is_valid = SudokuMethods.is_valid_board(board)
        if is_valid:
            return 'Valid', 202
        return 'Invalid', 406
    except AttributeError:
        return 'Invalid Request', 400
    except (Exception,):
        return 'Unknown Error', 500


if __name__ == "__main__":
    app.run(debug=True)
