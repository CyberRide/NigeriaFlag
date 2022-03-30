#Nigeria Flag Using Python

from PIL import Image, ImageDraw
import turtle

green = (0, 128, 0)
white = (255, 255, 255)
green = (0, 128, 0)

def nigeria (fname, width=400, height=300):
    flag= Image.new("RGB", (width, height))
    p,q= width//3, 2 * width //3
    draw= ImageDraw.Draw(flag)
    draw.rectangle((0,0,p,height),green)
    draw.rectangle((p,0,q,height),white)
    draw.rectangle((q,0,width,height),green)
    flag.save(fname)
nigeria("nigeria.gif")
tr= turtle.Turtle()
wm= turtle.Screen()
turtle.bgcolor('light green')
wm.addshape('nigeria.gif')
tr.shape('nigeria.gif')
wm.mainloop()