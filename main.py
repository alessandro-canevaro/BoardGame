#Main file from where the whole game is run

from components.Game_engine import GameEngine
from components.AI_agent import Agent


def main():
    ge = GameEngine()
    ge.setRandomNumberInTile(k=2)
    while True:
        ge.printboard()
        move = ''
        while move not in ['l', 'r', 'd', 'u']:
            move = input("Please select your next move (l, r, u, d):").lower()
        ge.swipe(move)
        ge.setRandomNumberInTile(k=1)
        if ge.isGameOver():
            print("Game over!")
            break
        elif ge.TestGoal():
            print("Victory!")
            break





if __name__ == "__main__":
    main()

#do stuff...