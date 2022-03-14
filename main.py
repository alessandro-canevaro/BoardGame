#Main file from where the whole game is run

from components.Game_engine import GameEngine
from components.ExpectiMax import ExpectiMaxAgent

def main():
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    em = ExpectiMaxAgent(ge.board, heuristic='snake')
    i = 0
    while i <= 10000:
        ge.printBoard()

        if ge.isGameOver():
            print("Game over!")
            break
        #elif ge.isGoal():
        #    print("Victory!")
        #    break

        em_move = em.ComputeNextMove()
        print("Move: {}: Score: {} AI suggests: {}".format(i, int(ge.board.score), em_move))
        #move = ''
        #possible_moves = ge.board.PossibleMoves()
        #while move not in possible_moves:
        #    move = input("Select your next move {}:".format(possible_moves)).lower()
        #ge.board.Swipe(move, True)
        ge.board.Swipe(em_move, True)
        ge.setRandomNumberInTile(k=1)
        em.UpdateTree(ge.board, em_move)
        i += 1


if __name__ == "__main__":
    main()

#do stuff...