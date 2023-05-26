# main.py

from graphics import *
import time
from widgets import storytell
from play import play
import time

# 
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def main():
  
    # if continueGame becomes False, we terminate a game and check the variable lost
    continueGame = True
    # if lost is True then we show a person that he lost
    # if lost is False but the game got terminated then he won
    lost = False
    # we enter the timer

    #creating a window
    win = GraphWin("Escape Room", 600, 400)
    win.setCoords(0, 0, 30, 20)
    win.setBackground('brown')

    inventory = []

    #starting timer
    startTime = time.time()
    
    # The main function that keeps the game going
    while continueGame == True:
        # play is a function defined in play.py
        # play returns continueGame and lost variables in case something changes in them
      continueGame, lost = play(win, inventory)


    endTime = time.time()
    timepassed = endTime - startTime

    if lost:
        storytell(win, "Tu tenias {} segundos para finalizar el juego y perdiste!".format(round(timepassed)))
    else:
        storytell(win, "Tu tenias {} segundos para finalizar el juego y ganaste!".format(round(timepassed)))

    win.close()

if __name__ == '__main__':
    main()
