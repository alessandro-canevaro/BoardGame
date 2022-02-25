from Utilities import Moves

class Agent:
    def __init__(self) -> None:
        pass

    def ExpandTree(self) -> None:
        pass

    def ComputeHeuristics(self) -> None:
        pass

    def ComputeNextMove(self) -> int:
        return Moves.up

if __name__ == "__main__":
    print("Do some tests...")
    agent = Agent()
    print(agent.ComputeNextMove())
    print("All done")