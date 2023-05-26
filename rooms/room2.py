# room2.py
# The function draws and activates a room2
import sys
sys.path.append("..")
from graphics import *
from button import Button
from widgets import storytell, test_code
import math
import random
import sympy as sp


def generar_funcion():
    grado = random.randint(1, 3)
    coeficientes = [random.randint(-10, 10) for _ in range(grado + 1)]
    x = sp.symbols('x')
    funcion = 0
    for i in range(grado + 1):
        funcion += coeficientes[i] * x**(grado - i)
    return funcion

funcion_aleatoria = generar_funcion()
print("Función generada:", funcion_aleatoria)

def metodo_biseccion(a, b, epsilon):
    x = sp.symbols('x')
    
    funcion = sp.lambdify(x, funcion_aleatoria)  # Convierte la expresión simbólica en una función evaluatable
    if funcion(a) * funcion(b) >= 0:
        print("El método de bisección no es aplicable en este intervalo.")
        return None

    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if funcion(c) == 0:
            break
        if funcion(a) * funcion(c) < 0:
            b = c
        else:
            a = c

    return c

a = 1
b = 2
epsilon = 0.0001

solucion = metodo_biseccion(a, b, epsilon)

if solucion is not None:
    print("La solución aproximada es:", solucion)
else:
    print("No se pudo encontrar una solución en el intervalo dado.")




def room2(win, inventory):
  # setting base variables
  continueGame = True
  lost = False

  # drawing room
  img2 = Image(Point(20, 10), "rooms/room2.gif")
  img2.draw(win)

  # drawing user
  user = Image(Point(30,2), "rooms/thief.gif")
  user.draw(win)

  # drawing inventory label
  inventLabel = Text(Point(5, 19), "")
  inventLabel.setStyle("bold")
  inventLabel.draw(win)

  get_item = Button(win, Point(5, 2), 8, 2, "Tomar el objeto <G>")
  # drawing a button that says that a person can observe a place by pressing o
  observe = Button(win, Point(5, 5), 8, 2, "Observar <O>")

  # drawing inventory items
  inventoryTexts = []
  last = 17
  for x in inventory:
      inventoryTexts.append(Text(Point(5, last), x))
      last = last - 1
  for x in inventoryTexts:
      x.draw(win)

  observed = False

  things_in_room = {"Point(27.0,11.0)": "Llave", "Point(18.0,14.0)": "Magia"}
  observe_in_room = {"Point(14.0,3.0)": "El Amuleto Desbloqueador (Alohomora), también conocido como el Amigo del Ladrón, era un amuleto que desbloqueaba objetos como puertas o ventanas. También fue capaz de abrir puertas cerradas por el Hechizo de Bloqueo (Colloportus), y como tal, actuó como su contra-encanto."}

  storytell(win, "Entras a otra habitacion")
  while continueGame is True and lost is False:
      # ask for key input (arrows)
      k = win.getKey()
      # check which arrow was pressed and move the user accordingly
      # while also checking that the user doesn't go outside the room's
      # borders
      if k == "Right" and user.getAnchor().getX() != 31:
          user.move(1, 0)
      if k == "Left" and user.getAnchor().getX() != 15:
          user.move(-1, 0)
      if k == "Up" and user.getAnchor().getY() != 14:
          user.move(0, 1)
      if k == "Down" and user.getAnchor().getY() != 2:
          user.move(0, -1)

      # key for getting an item
      if k == 'G' or k == 'g':
          if get_item.active:
              inventory.append(item)
              inventoryTexts.append(Text(Point(5, last), item))
              last = last - 1
              inventoryTexts[-1].draw(win)

      # key for observing an item
      if k == 'O' or k == 'o':
          if observe.active:
              storytell(win,observed_display)

      # Getting user location
      usx = user.getAnchor().getX()
      usy = user.getAnchor().getY()

      user_pos = "Point({0},{1})".format(usx, usy)

      # Activating a pickup button if the user is standing on an item that they can pick up.
      if user_pos in things_in_room.keys() and things_in_room[user_pos] not in inventory:
          item = things_in_room[user_pos]
          get_item.activate()
      else:
          get_item.deactivate()

      # activating an observe button if the user is standing on an item that they can observe.
      if user_pos in observe_in_room.keys():
          observed_display = observe_in_room[user_pos]
          observe.activate()
      else:
          observe.deactivate()

      # checking the door
      if usx >= Point(23.0, 14.0).getX() and usx <= Point(24.0, 14.0).getX() and usy >= Point(25.0,14.0).getY() and usy <= Point(26.0, 14.0).getY():
          # checking if a user has essential item
          if observed:
              # delete the room picture on the screen
              storytell(win,"Buen trabajo! Tu pasaste la segunda habitacion!")
              user.undraw()
              img2.undraw()
              for i in inventoryTexts:
                  i.undraw()
              get_item.undrawButton(win)
              observe.undrawButton(win)
              # and return the state
              return True, False, inventory
          else:
              print(str(solucion))
              storytell(win, "Resuelve la siguiente funcion por bisectriz")
              observed = test_code(win, funcion_aleatoria, str(solucion))
              if observed:
                storytell(win, "Correcto, no olvidas nada.")

  return continueGame, lost, inventory
