from sketchpy import canvas
from turtle import Screen
s=Screen()
s.bgcolor("Red")

ab=canvas.sketch_from_svg("C:\Users\NN Creations\AppData\Local\Programs\Python\Python311\Lib\shivji.svg",scale=45)
ab.draw()
