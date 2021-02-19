import numpy as np
from graphics import *

def main():
    Win=GraphWin("My Window",500,500)
    Win.setBackground(color_rgb(255,255 ,0))
    for i in range(2,498):
        for j in range(2,498):

            pt = Point(i, j)
            #r=np.random.uniform(20,40)
            cir = Circle(pt, 50)
            cir.setFill(color_rgb(255, 100, 200))
            cir.draw(Win)

    Win.getMouse()
    Win.close()
main()







