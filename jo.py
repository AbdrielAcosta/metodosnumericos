'''
Created on 11 may. 2023

@author: ja_ab
'''

class line:
    def __init__(self, length, x, y):
        self.length = length
        self.x = x 
        self.y = y
    def draw(self):
        print('drawing')
    def display(self):
        print('display')
        
Line1 = line(5,1,1)
print(Line1.length)
Line1.draw()