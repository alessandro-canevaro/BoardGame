#Main file from where the whole game is run

from components.Game_engine import GameEngine
from components.AI_agent import Agent

def main():
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    while True:
        ge.printboard()

        if ge.isGameOver():
            print("Game over!")
            break
        elif ge.isGoal():
            print("Victory!")
            break

        move = ''
        possible_moves = ge.board.PossibleMoves()
        while move not in possible_moves:
            move = input("Select your next move {}:".format(possible_moves)).lower()
        ge.board.Swipe(move)
        ge.setRandomNumberInTile(k=1)


if __name__ == "__main__":
    main()

#do stuff...