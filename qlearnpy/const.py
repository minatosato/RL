#!/usr/local/bin python
# -*- coding:utf-8 -+-

EPSILON_RATE = 0.3
LEARNING_RATE = 0.1
DISCOUNT_RATE = 0.9
SCR_X = 45*13 #スクリーンサイズ
SCR_Y = 45*10 #スクリーンサイズ
CS = 45 #セルのサイズ
NUM_ROW = SCR_Y/CS
NUM_COL = SCR_X/CS
START_X = 1
START_Y = 2
"""
FIELD = [[2 for x in range(NUM_COL)] for y in range(NUM_ROW)]
for y in range(NUM_ROW):
	for x in range(NUM_COL):
		if x==0 or y==0 or x==NUM_COL-1 or y==NUM_ROW-1:
			FIELD[y][x] = 3
"""

# row0 = [3,3,3,3,3,3]
# row1 = [3,2,2,2,2,3]
# row2 = [3,2,3,3,1,3]
# row3 = [3,3,3,3,3,3]


# row0 = [3,3,3,3,3,3,3]
# row1 = [3,2,2,2,2,3,3]
# row2 = [3,2,2,3,2,2,3]
# row3 = [3,2,3,2,3,2,3]
# row4 = [3,2,2,2,3,2,3]
# row5 = [3,2,3,2,3,2,3]
# row6 = [3,2,3,2,2,2,3]
# row7 = [3,2,3,2,3,2,3]
# row8 = [3,2,2,2,3,1,3]
# row9 = [3,3,3,3,3,3,3]

row0 = [3,3,3,3,3,3,3,3,3,3,3,3,3]
row1 = [3,2,2,2,2,2,3,3,3,2,2,2,3]
row2 = [3,2,2,3,2,2,2,2,2,2,3,2,3]
row3 = [3,2,3,2,3,3,3,2,3,2,2,2,3]
row4 = [3,2,2,2,3,2,2,2,3,2,3,2,3]
row5 = [3,2,3,2,3,2,3,2,3,2,2,2,3]
row6 = [3,2,3,2,2,2,3,2,2,2,3,2,3]
row7 = [3,2,3,2,3,2,2,2,3,2,3,2,3]
row8 = [3,2,2,2,3,2,3,2,2,2,3,1,3]
row9 = [3,3,3,3,3,3,3,3,3,3,3,3,3]

FIELD = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9]
# FIELD = [row0,row1,row2,row3]

