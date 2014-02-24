#!/usr/local/bin python
# -*- coding:utf-8 -+-

import const
import pygame
from pygame.locals import *
import random
import sys
import state
import agent
import action

SCR_RECT = Rect(0,0,const.SCR_X,const.SCR_Y)
CS = const.CS
NUM_ROW = SCR_RECT.height / CS   # フィールドの行数
NUM_COL = SCR_RECT.width / CS  # フィールドの列数
START = 0
GOAL = 1
ROAD = 2
WALL = 3
CS_COLOR = (255,255,255)
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class Map:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption(u"Q-Learning")
        self.font = pygame.font.SysFont('Ricty',42)
        self.field = [[state.State(GOAL)for x in range(NUM_COL)] for y in range(NUM_ROW)]
        self.agent = agent.Agent()
        self.state = self.field[self.agent.y][self.agent.x]
        self.generation = 0
        self.agentx = self.agent.x
        self.agenty = self.agent.y
        self.run = False
        self.learn = False
        self.cursor = [NUM_COL/2, NUM_ROW/2]
        self.clear()
        self.set_all_possibility()
        clock = pygame.time.Clock()
        self.draw(self.screen)
        while True:
            #clock.tick(100)
            self.update()
            self.draw(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key==K_s:
                        self.run = not self.run
                    elif event.key==K_n:
                        self.step()
                    elif event.key==K_l:
                        self.learn = not self.learn
                    elif event.key == K_LEFT:
                        self.cursor[0] -= 1
                        if self.cursor[0] < 0: self.cursor[0] = 0
                    elif event.key == K_RIGHT:
                        self.cursor[0] += 1
                        if self.cursor[0] > NUM_COL-1: self.cursor[0] = NUM_COL-1
                    elif event.key == K_UP:
                        self.cursor[1] -= 1
                        if self.cursor[1] < 0: self.cursor[1] = 0
                    elif event.key == K_DOWN:
                        self.cursor[1] += 1
                        if self.cursor[1] > NUM_ROW-1: self.cursor[1] = NUM_ROW-1
                    elif event.key == K_SPACE:
                        x, y = self.cursor
                        print '-----------------------------------'
                        print '      %05.2f' %self.field[y][x].action[2].q
                        print '%05.2f' %self.field[y][x].action[0].q,
                        print '       %05.2f' %self.field[y][x].action[1].q
                        print '      %05.2f' %self.field[y][x].action[3].q
                        print '-----------------------------------'
    #init
    def clear(self):
        self.generation = 0
        self.agent = agent.Agent()
        self.agentx = self.agent.x
        self.agenty = self.agent.y
        self.state = self.field[self.agent.y][self.agent.x]        
        for y in range(NUM_ROW):
            for x in range(NUM_COL):
                self.field[y][x] = state.State(const.FIELD[y][x])
                if const.FIELD[y][x]==GOAL:
                    self.field[y][x].r = 100

    def draw(self, screen):
        #print("debug draw")
        for y in range(NUM_ROW):
            for x in range(NUM_COL):
                if self.field[y][x].k == WALL:
                    pygame.draw.rect(screen,(0,0,0),Rect(x*CS,y*CS,CS,CS))
                elif self.field[y][x].k == ROAD:
                    pygame.draw.rect(screen,CS_COLOR,Rect(x*CS,y*CS,CS,CS))
                    if self.field[y][x].get_max_q_action().q != 0:
                        val = self.field[y][x].get_max_q_action().q/100.0
                        # if val > 1:
                        #     val = 1
                        val *= 255.0
                        color = (255,255-val,255-val)
                        pygame.draw.rect(screen,color,Rect(x*CS,y*CS,CS,CS))
                        num = self.field[y][x].get_max_q_action().d
                        direction = u""
                        if num==UP:
                            direction = u"↑"
                        elif num==DOWN:
                            direction = u"↓"
                        elif num==LEFT:
                            direction = u"←"
                        else:
                            direction = u"→"
                        screen.blit(self.font.render(direction, True, (0,0,0)), (x*CS,y*CS))
                elif self.field[y][x].k == GOAL:
                    pygame.draw.rect(screen,(100,255,255),Rect(x*CS,y*CS,CS,CS))
                if y == self.agenty and x == self.agentx:
                    pygame.draw.rect(screen,(0,0,255),Rect(x*CS,y*CS,CS,CS))
                pygame.draw.rect(screen,(50,50,50),Rect(x*CS,y*CS,CS,CS),1)
        pygame.draw.rect(screen, (0,255,0), Rect(self.cursor[0]*CS,self.cursor[1]*CS,CS,CS), 5)

    def step(self):
        self.action = self.state.action_select()
        self.agent.move(self.action)
        self.state = self.field[self.agent.y][self.agent.x]
        self.action.update_q_value(self.state)
        self.agentx = self.agent.x
        self.agenty = self.agent.y
        if self.state.k == 1:
            self.agent.move_start()
            self.state = self.field[self.agent.y][self.agent.x]

    def update(self):
        if self.run == True and self.learn == False:
            self.step()
        elif self.learn == True:
            self.step()

    def set_possibility(self,y,x):
        if self.field[y][x].k == ROAD or self.field[y][x].k == START or self.field[y][x].k == GOAL:
            if self.field[y][x-1].k==ROAD or self.field[y][x-1].k==GOAL or self.field[y][x-1].k==START:
                self.field[y][x].set_action(LEFT,True)
            if self.field[y][x+1].k==ROAD or self.field[y][x+1].k==GOAL or self.field[y][x+1].k==START:
                self.field[y][x].set_action(RIGHT,True)
            if self.field[y-1][x].k==ROAD or self.field[y-1][x].k==GOAL or self.field[y-1][x].k==START:
                self.field[y][x].set_action(UP,True)
            if self.field[y+1][x].k==ROAD or self.field[y+1][x].k==GOAL or self.field[y+1][x].k==START:
                self.field[y][x].set_action(DOWN,True)

    def set_all_possibility(self):
        for y in range(1,NUM_ROW-1):
            for x in range(1,NUM_COL-1):
                self.set_possibility(y,x)

if __name__ == '__main__':
	Map()
