# room4.py
# The function draws and activates a room4
import sys
sys.path.append("..")
from graphics import *
from button import Button
from widgets import storytell, test_code


def room4(win, inventory):
    # setting base variables
    continueGame = True
    lost = False

    # drawing room
    img4 = Image(Point(20, 10), "rooms/room4.gif")
    img4.draw(win)

    # drawing user
    user = Image(Point(29.0,6.0), "rooms/thief.gif")
    user.draw(win)

    # drawing inventory label
    inventLabel = Text(Point(5, 19), "Inventario")
    inventLabel.setStyle("bold")
    inventLabel.draw(win)

    # drawing a button that says that a person can put an item into inventory by pressing g
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

    # test passed is what a user needs to get the main_item
    test_passed = False
    main_item = 'remote control'

    # things_in_room is a list of items present in that room. (only one of them is necessary)
    things_in_room = {"Point(19.0,6.0)": "Control remoto"}
    observe_in_room = {"Point(21.0,14.0)": "La pantalla dice: '¿Puedes responder cuántos meses tienen 28 días?'"}


  # storytell before the room begins
    storytell(win, "¿Qué tipo de habitación es esta? Los ricos son raros ... ¿Tal vez la televisión tiene algo?")
    while continueGame is True and lost is False:

        # ask for key input (arrows)
        k = win.getKey()
        # check which arrow was pressed and move the user accordingly
        # while also checking that the user doesn't go outside the room's
        # borders
        if k == "Right" and user.getAnchor().getX() != 30:
            user.move(1, 0)
        if k == "Left" and user.getAnchor().getX() != 10:
            user.move(-1, 0)
        if k == "Up" and user.getAnchor().getY() != 20:
            user.move(0, 1)
        if k == "Down" and user.getAnchor().getY() != 0:
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
                test_passed = test_code(win, observed_display, "12")

        # Getting user location
        usx = user.getAnchor().getX()
        usy = user.getAnchor().getY()

        user_pos = "Point({0},{1})".format(usx, usy)

        # Activating a pickup button if the user is standing on an item that they can pick up.
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

        # activating an observe button if the user is standing on an item that they can observe.
        if user_pos in observe_in_room.keys():
            observed_display = observe_in_room[user_pos]
            observe.activate()
        else:
            observe.deactivate()


            # checking if a user has essential item
        if test_passed and main_item in inventory:
            # delete the room picture on the screen
            storytell(win,"¡Buen trabajo! Pasaste por la cuarta habitación porque el acertijo que resolviste activó el control remoto y pudiste desbloquear una puerta oculta debajo de la cama.")
            user.undraw()
            img4.undraw()
            for i in inventoryTexts:
                i.undraw()
            get_item.undrawButton(win)
            observe.undrawButton(win)
            # and return the state
            return True, False, inventory

    return continueGame, lost, inventory
