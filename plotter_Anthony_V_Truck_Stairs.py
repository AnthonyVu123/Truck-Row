# Anthony Vu
from madison_axi.axi import*
initialize()
from random import randrange
from random import choice

move_to(-250,180)
def body():
 point_in_direction(360)
 pen_down()
 for x in range(1,180):
   move_forward(1)
   turn_right(2)
  
def circle():
 point_in_direction(360)
 pen_down()
 move_forward(150)
 for x in range(1,180):
   move_forward(1)
   turn_right(2)

def rectangle():
 point_in_direction(360)
 for x in range(1,3):
  move_forward(50)
  turn_left(90)

 move_forward(300)
 turn_left(90)
 move_forward(50)
 turn_left(90)
 move_forward(100)

def window():
 pen_up()
 point_in_direction(90)
 move_forward(50)
 turn_right(90)
 move_forward(150)
 pen_down()
 for x in range(1,4):
  turn_left(90)
  move_forward(50)

def flag():
 pen_up() 
 turn_left(90)
 move_forward(25)
 turn_left(90)
 move_forward(50)
 pen_down()
 move_forward(100)
 turn_right(90)
 move_forward(75)
 turn_right(90)
 move_forward(75)
 turn_right(90)
 move_forward(75)

def shape_of_flag():
 pen_up()
 turn_right(90)
 move_forward(37)
 turn_right(90)
 move_forward(37)
 pen_down()

def truck():
  poly = choice([3,5,6,8,9,10])
  size = randrange(5,15)
  body()
  circle()
  rectangle()
  window()
  flag()
  shape_of_flag()
  for angle in range(0,poly):
   move_forward(size)
   turn_left(360/poly)  

for x in range(0,4):   
    truck()
    pen_up()
    point_in_direction(270)
    move_forward(270)
cleanup()

