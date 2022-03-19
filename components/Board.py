import numpy as np


class Board:
    def __init__(self, board=None, board_size=4) -> None:
        self.board_size = board.board_size if board else board_size
        self.values = board.values.copy() if board else np.zeros((self.board_size, self.board_size), dtype=int)
        self.score = 0

    def __repr__(self) -> str:
        return str(self.values)

    def __iter__(self):
        return iter(self.values)

    def __eq__(self, board_obj) -> bool:
        return np.array_equal(self.values, board_obj.values)

    def GetMaxTileValue(self):
        return np.max(self.values)

    def PossibleMoves(self) -> list:
        """Return a list with the possible moves between l, r, u, d.
        """
        possible_moves = []
        for direction in ['left', 'right', 'up', 'down']:
            new_board = self.Swipe(direction, False, inplace=False)
            if not np.array_equal(self.values, new_board):
                possible_moves.append(direction)
        return possible_moves

    def GetEmptyTiles(self) -> list:
        """Return a list of tuple representing the position of the empty tiles.
        """
        return list(zip(*np.where(self.values == 0)))

    def SetEmptyTile(self, position, value) -> None:
        """Set an empty tile with 'value'
        """
        if position in self.GetEmptyTiles():
            self.values[position] = value

    def _compress(self, row) -> list:
        """compress all the numbers on one side of the board.
        """
        new_row = [i for i in row if i != 0]
        return new_row + [0] * (self.board_size - len(new_row))

    def _swiperow(self, row, score_update=False) -> list:
        """return the row after a swipe from right to left.
        """
        row = self._compress(row)
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                row[i] = row[i] * 2
                if score_update:
                    self.score += row[i]
                row[i + 1] = 0
        return self._compress(row)

    def _swiperowEfficient(self, row, score_update):
        new_row = row[np.nonzero(row)]
        diff = np.diff(new_row) == 0
        new_row[diff.nonzero()] *= 2
        new_row[diff.nonzero()[0] + 1] = 0
        new_row = new_row[np.nonzero(new_row)]
        padded_array = np.zeros_like(row)
        padded_array[:new_row.shape[0]] = new_row
        return padded_array

    def _swipeLeft(self, board_values, score_update) -> np.ndarray:
        new_board = np.zeros_like(board_values)
        for i in range(self.board_size):
            new_board[i, :] = self._swiperow(board_values[i, :], score_update)
        return new_board

    def Swipe(self, direction, score_update, inplace=True):
        moves2rot = {'left': (0, 4),
                     'up': (1, 3),
                     'right': (2, 2),
                     'down': (3, 1)}

        new_board = np.rot90(self.values, moves2rot[direction][0])
        new_board = self._swipeLeft(new_board, score_update)
        new_board = np.rot90(new_board, moves2rot[direction][1])

        if inplace:
            self.values = new_board
        else:
            return new_board


if __name__ == "__main__":
    b = Board