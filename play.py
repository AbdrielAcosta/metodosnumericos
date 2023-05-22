# play.py

from rooms.room1 import room1
from rooms.room2 import room2
from rooms.room3 import room3
from rooms.room4 import room4
from rooms.room5 import room5


def play(win, inventory):
    lost = False
    continueGame = True

    rooms = [room1, room2, room3, room4, room5]
    i = 0
    while continueGame == True:
      # first room gets activated
      continueGame, lost, inventory = rooms[i](win, inventory)
      i = i + 1
    return continueGame, lost

