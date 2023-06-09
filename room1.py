# room1.py
# The function draws and activates a room1
import sys
sys.path.append("..")
from graphics import *
from button import Button
from widgets import storytell
import time

def room1(win, inventory):

# setting base variables
  continueGame = True
  lost = False

# drawing room
  img1 = Image(Point(20, 10), "rooms/room1.gif")
  img1.draw(win)

# drawing user
  user = Image(Point(20,1), "rooms/thief.gif")
  user.draw(win)

# drawing inventory label
  inventLabel = Text(Point(5, 19), "Inventario")
  inventLabel.setStyle("bold")
  inventLabel.draw(win)

# drawing a button that says that a person can put an item into inventory by pressing g
  get_item = Button(win, Point(5,2), 8, 2, "Tomar el objeto <G>")

# drawing inventory items
  inventoryTexts = []
  last = 17
  for x in inventory:
      inventoryTexts.append(Text(Point(5,last), x))
      last = last - 1
  for x in inventoryTexts:
      x.draw(win)

  # setting up the key items for the room and what can be collected
  main_item = 'vela'
  things_in_room = {"Point(25.0,12.0)": "vela",  "Point(12.0,2.0)": "plant"}

# storytell


  # Storytell The beginning
  storytell(win,
        "Trata de escapar")
  storytell(win, "Te puedes mover con las flechas")
  storytell(win,
        " ")
  storytell(win, "")


  while continueGame is True and lost is False:


      k = win.getKey()
     
      if k == "Right" and user.getAnchor().getX() != 32:
          user.move(1, 0)
      if k == "Left" and user.getAnchor().getX() != 14:
          user.move(-1, 0)
      if k == "Up" and user.getAnchor().getY() != 20:
          user.move(0, 1)
      if k == "Down" and user.getAnchor().getY() != 0:
          user.move(0, -1)

      if k == 'G' or k == 'g':
        if get_item.active:
            inventory.append(item)
            inventoryTexts.append(Text(Point(5, last), item))
            last = last - 1
            inventoryTexts[-1].draw(win)

      # Getting user location
      usx = user.getAnchor().getX()
      usy = user.getAnchor().getY()

      user_pos = "Point({0},{1})".format(usx, usy)
      # Activating a pickup button if the user is standing on a vela
      if user_pos in things_in_room.keys() and things_in_room[user_pos] not in inventory:
          item = things_in_room[user_pos]
          get_item.activate()
      else:
          get_item.deactivate()
        
      # checks that if user tries to go through the 
      # left door, he/she dies
      if usx == Point(10.0, 7.0).getX() and usy == Point(10.0, 7.0).getY():
        storytell(win,"The thief went into the living room and the dog got woken up and barked till the neighbours came. You loose! The thief got arrested.")
        continueGame = False
        lost = True

      # checking the ladder
      if usx >= Point(10.0, 17.0).getX() and usx<= Point(16.0, 17.0).getX() and usy >= Point(10.0, 17.0).getY() and usy <= Point(10.0, 20.0).getY():
          # checking if a user has essential item
          if main_item in inventory:
              # delete the room picture on the screen
              storytell(win,"¡Buen trabajo! ¡Pasaste la primera habitación con la ayuda de la vela en tu inventario! Ahora es el momento de la siguiente habitación. ")
              user.undraw()
              img1.undraw()
              for i in inventoryTexts:
                  i.undraw()
              get_item.undrawButton(win)
              # and return the state
              return True, False, inventory
          else:
              storytell(win,"Las escaleras estaban demasiado oscuras y el ladrón se cayó, abrió la cabeza y quedó inconsciente hasta que los dueños regresaron. Luego, fue arrestado.")
              return False, True, inventory

  return continueGame, lost, inventory
