#!/usr/local/bin python
# -*- coding:utf-8 -+-

import const

class Agent:
    def __init__(self):
        self.current_x = const.START_X
        self.current_y = const.START_Y
    def getx(self):
        return self.current_x
    def setx(self, value):
        self.current_x = value
    x = property(getx, setx)

    def gety(self):
        return self.current_y
    def sety(self, value):
        self.current_y = value
    y = property(gety, sety)

    def move(self,action):
        poss = action.p
        direction = action.d
        if direction==0 and poss==True:
            self.current_x -= 1
        elif direction==1 and poss==True:
            self.current_x += 1
        elif direction==2 and poss==True:
            self.current_y -= 1
        elif direction==3 and poss==True:
            self.current_y += 1

    def move_start(self):
        self.current_x = const.START_X
        self.current_y = const.START_Y
