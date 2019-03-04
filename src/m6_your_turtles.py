"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Montgomery Winslow.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

star = rg.SimpleTurtle()
star.pen = rg.Pen('green' , 10)

circle = rg.SimpleTurtle()
circle.pen = rg.Pen('blue' , 5)
circle.pen_up()

for k in range(5) :
    star.left(72 * 2)
    circle.left(72*2)
    star.forward(200)
    circle.go_to(rg.Point(star.x_cor() , star.y_cor()))
    circle.left(90)
    circle.forward(5)
    circle.pen_down()
    circle.draw_circle(10) #I'm not quite sure how to properly center it
    circle.pen_up()
    circle.right(90)
    circle.forward(5)
window.close_on_mouse_click()
