# room3.py
# The function draws and activates a room3
import sys
sys.path.append("..")
from graphics import *
from button import Button
from widgets import storytell

def room3(win, inventory):

  # setting base variables
    continueGame = True
    lost = False

  # drawing room
    img3 = Image(Point(20, 10), "rooms/room3.gif")
    img3.draw(win)

  # drawing user
    user = Image(Point(20,1), "rooms/thief.gif")
    user.draw(win)
  
  # drawing inventory label
    inventLabel = Text(Point(5, 19), "Inventory")
    inventLabel.setStyle("bold")
    inventLabel.draw(win)

  # drawing a button that says that a person can put an item into inventory by pressing g
    get_item = Button(win, Point(5,2), 8, 2, "Get Item by Pressing <g>")
  # drawing a button that says that a person can observe a place by pressing o
    observe = Button(win, Point(5, 5), 8, 2, "Observe by Pressing <o>")

  # drawing inventory items
    inventoryTexts = []
    last = 17
    for x in inventory:
        inventoryTexts.append(Text(Point(5, last), x))
        last = last - 1
    for x in inventoryTexts:
        x.draw(win)

    # observed is what a user needs to proceed to the next level
    main_item = "cake"
  
  #set the points of the items
    things_in_room = {"Point(12.0,11.0)": "cake", "Point(17.0,14.0)": "towel"}
    observe_in_room = {"Point(22.0,15.0)": "Mom, the piece of the puzzle is hidden in the kitchen! It should be a piece of cake. Be careful when opening the fridge, it’s extremely cold!"}


    # storytell
  # storytelling the beginning of room3
    storytell(win,"The kitchen! This is making me hungry... I wish I could sit down but I have to keep going because I don't have much time left! What could possibly be the hidden piece in this room? I see a fridge, a glass of milk, a cup of tea, a TV... mmm")
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
                if item == 'cake':
                    if "towel" not in inventory:
                        storytell(win, "The fridge was so cold that your hand got stuck to its doorknob and the thief got caugth.")
                        return False, True, inventory
                inventory.append(item)
                inventoryTexts.append(Text(Point(5, last), item))
                last = last - 1
                inventoryTexts[-1].draw(win)

        # key for observing an item
        if k == 'O' or k == 'o':
            if observe.active:
                storytell(win, observed_display)
                storytell(win, "Hmm… what does she mean by that? Maybe I should look for something to open the fridge with. Don’t wanna risk getting caught…")
                observed = True

        # Getting user location
        usx = user.getAnchor().getX()
        usy = user.getAnchor().getY()

        user_pos = "Point({0},{1})".format(usx, usy)
        
      # Activating a pickup button if the user is standing on an item that they can pick up
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

        # checking if a user has essential item
        if main_item in inventory:
            # delete the room picture on the screen
            storytell(win,"Good Job! You passed the third room because you figured out that you would need a towel to open the fridge, and you also got the 'cake' mentioned in hint.")
            user.undraw()
            img3.undraw()
            for i in inventoryTexts:
                i.undraw()
            get_item.undrawButton(win)
            observe.undrawButton(win)
            # and return the state
            return True, False, inventory

    return continueGame, lost, inventory
