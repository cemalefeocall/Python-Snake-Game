from turtle import Turtle,Vec2D
from random import randint
from math import sqrt,pow
class Food(Turtle):
    # for setting random (x,y) coordinates of the food
    def setRandomXY(self):
        self.random_x = randint(-200,200)
        self.random_y = randint(-200,200)
        self.goto(self.random_x,self.random_y)

    def __init__(self):
        self.score = 0
        # Food initiliazers
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        # Random
        self.setRandomXY()
    #calculating distance between two points in 2D Space Private Func. Do not Call
    def calculateDistance(self,VEC1,VEC2):
        return sqrt(pow(VEC2[1]-VEC1[1],2) + pow(VEC2[0]-VEC1[0],2))
    def detectCollisionWithFood(self,snake_head_coordinates):
        if self.calculateDistance(snake_head_coordinates,self.pos()) < 20:
            self.setRandomXY()
            return True
        else:
            return False
    def increaseScoreValue(self):
        self.score += 1
    def getScoreValue(self):
        return self.score
