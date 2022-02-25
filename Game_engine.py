class GameEngine:

    def __init__(self) -> None:
        self.board = [[0 for i in range(4)] for j in range(4)]

    def TestGoal(self, goal=2048) -> bool:
        """Return True if the board contains the goal value.
        """
        return any(goal in row for row in self.board)

if __name__ == "__main__":
    ge = GameEngine()
    print(ge.TestGoal())
    ge.board[0][3] = 2048
    print(ge.TestGoal())
    print("all done")
