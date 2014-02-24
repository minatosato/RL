#!/usr/local/bin python
# -*- coding:utf-8 -+-

import const

class Action:
    def __init__(self, direction, possibility):
        self.q_value = 0.00
        self.possibility = possibility
        self.direction = direction
    def getd(self):
        return self.direction
    def setd(self, value):
        self.direction = value
    d = property(getd, setd)
    def getq(self):
        return self.q_value
    def setq(self, value):
        self.q_value = value
    q = property(getq, setq)
    def getp(self):
        return self.possibility
    def setp(self, value):
        self.possibility = value
    p = property(getp, setp)
    def set_possibility(self,direction,possibility):
        self.possibility = possibility
        self.direction = direction
    def update_q_value(self,state):
        alpha = const.LEARNING_RATE
        gamma = const.DISCOUNT_RATE
        r = state.r
        max_q = state.get_max_q_action().q
        self.q_value = self.q_value + alpha*(r+gamma*max_q-self.q_value)
