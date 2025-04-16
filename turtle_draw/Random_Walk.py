import turtle as t
import random

tim = t.Turtle()

###########  Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# 0 - east, 90 - north, 180 - west, 270 - south.
directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

