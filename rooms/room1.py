# room1.py
# The function draws and activates a room1
import sys
sys.path.append("..")
from graphics import *
from button import Button
from widgets import storytell
import time
import jo
import a1
from widgets import test_code

def room1(win, inventory):

# setting base variables
  continueGame = True
  lost = False

# drawing room
  img1 = Image(Point(20, 10), "rooms/room1.gif")
  img1.draw(win)

# drawing user
  user = Image(Point(20,2), "rooms/thief.gif")
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
  main_item = 'Vela'
  things_in_room = {"Point(31.0,3.0)": "Vela", "Point(15.0,3.0)": "Plant"}

  # storytell


  # Storytell The beginning
  storytell(win,
        "Trata de escapar de todas las habitaciones")
  storytell(win, "Te puedes mover con las flechas")
  storytell(win, "Avanza a traves de las salas resolviendo problemas numericos")
  storytell(win, "Al mismo tiempo que recoges objetos utiles para tu aventura")
  storytell(win, "¡Mucha Suerte!")


  while continueGame is True and lost is False:

      # ask for key input (arrows)
      k = win.getKey()
      # check which arrow was pressed and move the user accordingly 
      # while also checking that the user doesn't go outside the room's
      # borders
      if k == "Right" and user.getAnchor().getX() != 32:
          user.move(1, 0)
      if k == "Left" and user.getAnchor().getX() != 14:
          user.move(-1, 0)
      if k == "Up" and user.getAnchor().getY() != 16:
          user.move(0, 1)
      if k == "Down" and user.getAnchor().getY() != 2:
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
          cont = 0
          while (cont == 0):
              numrand = a1.rand()
              if (numrand not in jo.nMetodo):
                  metodo = a1.filt(numrand)
                  jo.nMetodo.append(numrand)
                  cont += 1
          print(str(a1.resolucion(numrand)))
          storytell(win, "Resuelve la siguiente funcion por" + metodo)
          observed = test_code(win, str(a1.problema(numrand)), str(a1.resolucion(numrand)))
          if observed:
              storytell(win, "Correcto, no olvidas nada.")
              item = things_in_room[user_pos]
              get_item.activate()
          else:
              continueGame = False
      else:
          get_item.deactivate()
        
      # checks that if user tries to go through the 
      # left door, he/she dies
      if usx == Point(14.0, 7.0).getX() and usy == Point(14.0, 8.0).getY():
        storytell(win,"El ladrón entró en la sala de estar y el perro se despertó y ladró hasta que llegaron los vecinos. ¡Pierdes! El ladrón fue arrestado.")
        continueGame = False
        lost = True

      # checking the ladder
      if usx >= Point(16.0, 16.0).getX() and usx<= Point(17.0, 16.0).getX() and usy >= Point(18.0, 16.0).getY() and usy <= Point(19.0, 16.0).getY():
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
