# widgets.py
from graphics import *
from button import Button
from dieview import DieView
from random import randrange
import time

# The function is basically given a window, a text that needs to be displayed on top of everything (pop up) and the length (how long we want the pop up to be visible {maybe instead of sleep we could create close button but lets leave it like this for now})
def storytell(win, text):
    Board = Rectangle(Point(2, 2), Point(28, 18))
    Board.setOutline("Black")
    Board.setWidth(2)
    Board.setFill('brown2')
    Board.draw(win)
    words = text.split(' ')
    sentence = ''
    sentences = []
    i = 0
    for word in words:
        sentence = sentence + " " + word
        i = i + 1
        if i % 10 == 0 or i == len(words):
            sentences.append(sentence)
            sentence = ''

    space = 1
    if len(sentences) % 2 == 1:
        start = 10 + space * len(sentences)/2
    else:
        start = 10 - space/2 + space * len(sentences)/2


    texts = []
    for i in range(len(sentences)):
        texts.append(Text(Point(15, start), sentences[i]))
        texts[i].draw(win)
        start = start - space

    quit_button = Button(win, Point(15.0, 4.0), 4, 2, "Close")
    quit_button.activate()
    pt = win.getMouse()

    if quit_button.clicked(pt):
        for i in texts:
            i.undraw()
        Board.undraw()
        quit_button.deactivate()
        quit_button.undrawButton(win)
      
    else:
      for i in texts:
            i.undraw()
        
      Board.undraw()
      quit_button.deactivate()
      quit_button.undrawButton(win)
      storytell(win, text)


def test_code(win, display, answer):
    Board = Rectangle(Point(2, 2), Point(28, 18))
    Board.setOutline("Black")
    Board.setWidth(2)
    Board.setFill('brown2')
    Board.draw(win)

    display = Text(Point(15.0, 12.0), display)
    display.draw(win)

    textEntry = Entry(Point(15.0, 6.0), 6)
    textEntry.draw(win)

    # click the mouse to signal done entering text or quitting
    enter = Button(win, Point(12, 4), 3, 2, "Enter")
    enter.activate()
    quit_button = Button(win, Point(18.0, 4.0), 3, 2, "Close")
    quit_button.activate()
    pt = win.getMouse()

    if enter.clicked(pt):
        text = textEntry.getText()
        testText = Text(Point(15, 6), text)
        testText.draw(win)
        if text == answer:
            textEntry.undraw()
            storytell(win, "Correct!")
            Board.undraw()
            testText.undraw()
            enter.undrawButton(win)
            enter.deactivate()
            quit_button.deactivate()
            quit_button.undrawButton(win)
            display.undraw()
            textEntry.undraw()
            return True
        else:
            textEntry.undraw()
            storytell(win, "Wrong. But you can try again.")
            Board.undraw()
            testText.undraw()
            enter.undrawButton(win)
            enter.deactivate()
            quit_button.deactivate()
            quit_button.undrawButton(win)
            display.undraw()
            
            return False

    if quit_button.clicked(pt):
        Board.undraw()
        enter.undrawButton(win)
        enter.deactivate()
        quit_button.deactivate()
        quit_button.undrawButton(win)
        display.undraw()
        textEntry.undraw()
        return False

    else:
      Board.undraw()
      enter.undrawButton(win)
      enter.deactivate()
      quit_button.deactivate()
      quit_button.undrawButton(win)
      display.undraw()
      textEntry.undraw()
      

def test_dice(win):
    Board = Rectangle(Point(2, 2), Point(28, 18))
    Board.setOutline("Black")
    Board.setWidth(2)
    Board.setFill('brown2')
    Board.draw(win)

    display = Text(Point(15.0, 15), "Roll the same dice")
    display.draw(win)
    die1 = DieView(win, Point(12, 12), 2)
    die2 = DieView(win, Point(18, 12), 2)
    rollButton = Button(win, Point(15, 8), 2, 1, "Roll")
    rollButton.activate()
    # Event loop
    pt = win.getMouse()
    while True:
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            if value2 == value1:
                time.sleep(1)
                Board.undraw()
                display.undraw()
                rollButton.undrawButton(win)
                return True
        pt = win.getMouse()
