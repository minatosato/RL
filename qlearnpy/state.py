#!/usr/local/bin python
# -*- coding:utf-8 -+-

import const
from action import *
import random

class State:
    def __init__(self,kind):
        self.reward = 0
        self.kind = kind
        self.action = [Action(0,False),Action(1,False),Action(2,False),Action(3,False)]

    def getr(self):
        return self.reward
    def setr(self, value):
        self.reward = value
    r = property(getr, setr)

    def getk(self):
        return self.kind
    def setk(self, value):
        self.kind = value
    k = property(getk, setk)

    def set_action(self,direction,possibility):
        self.action[direction].set_possibility(direction,possibility)

    def get_max_q_action(self):
        m = max(xrange(len(self.action)), key=lambda i: self.action[i].q)
        if self.action[0].q == 0.00 and self.action[1].q == 0.00 and self.action[2].q == 0.00 and self.action[3].q == 0.00:
            m = random.randint(0,3)
            # while True:
            #     m = random.randint(0,3)
            #     if self.action[m].p!=False:
            #         break
        return self.action[m]
    def action_select(self):
        choosen = 0
        if random.random() > const.EPSILON_RATE:
            choosen = self.get_max_q_action().d
        else:
            choosen = random.randint(0,3)
            # while True:
            #     choosen = random.randint(0,3)
            #     if self.action[choosen].p!=False:
            #         break
        return self.action[choosen]
