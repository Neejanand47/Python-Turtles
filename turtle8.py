import turtle # importing the module
trtl = turtle.Turtle() #making a turtle object of Turtle class for drawing
screen=turtle.Screen() #making a canvas for drawing
screen.setup(420,320) #choosing the screen size
screen.bgpic('bg.gif') #making canvas black
trtl.pencolor('red') #making colour of the pen red
trtl.pensize(4) #choosing the size of pen nib
trtl.speed(1) #choosing the speed of drawing
trtl.shape('turtle') #choosing the shape of pen nib
trtl.circle(60) #drawing circle with radius 60 pixels