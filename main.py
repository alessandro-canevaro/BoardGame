#Main file from where the whole game is run

from components.Game_engine import GameEngine
from components.ExpectiMax import ExpectiMaxAgent

def main():
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    em = ExpectiMaxAgent(ge.board)
    i = 0
    while i <= 1000:
        ge.printboard()

        if ge.isGameOver():
            print("Game over!")
            break
        elif ge.isGoal():
            print("Victory!")
            break

        em_move = em.ComputeNextMove()
        print("{}: AI suggests: {}".format(i, em_move))
        #move = ''
        #possible_moves = ge.board.PossibleMoves()
        #while move not in possible_moves:
        #    move = input("Select your next move {}:".format(possible_moves)).lower()
        ge.board.Swipe(em_move)
        ge.setRandomNumberInTile(k=1)
        em.UpdateTree(ge.board)
        i += 1


if __name__ == "__main__":
    main()

#do stuff...