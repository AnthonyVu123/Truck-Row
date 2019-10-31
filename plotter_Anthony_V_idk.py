from madison_axi.axi import*
initialize()

#truck
move_to(-250,0)
pen_down()
for x in range(1,20):
  move_forward(1 * x)
  turn_right(120)
  
#circle
pen_up()  
move_to(0,0)
pen_down()
move_forward(100)
turn_right(1)
cleanup()
