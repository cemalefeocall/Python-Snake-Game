from turtle import Turtle
from math import sqrt,pow
class Snake:
    def __init__(self):
        # initial snake
        self.snake_segments = []
        for j in range(3):
            pieces = Turtle(shape="square")
            pieces.color("white")
            pieces.penup()
            pieces.setpos(j*-20,0)
            self.snake_segments.append(pieces)
            self.snake_head = self.snake_segments[0]
    def addSnakeSegments(self):
        piece = Turtle(shape="square")
        piece.color("white")
        piece.penup()
        self.snake_segments.append(piece)
    def getSnakeLength(self) -> int:
        return len(self.snake_segments)
    def calculateDistance(self,VEC1,VEC2):
        return sqrt(pow(VEC2[1]-VEC1[1],2) + pow(VEC2[0]-VEC1[0],2))
    def WallColision(self):
        current_x_cor = self.snake_head.xcor()
        current_y_cor = self.snake_head.ycor()
        if current_x_cor == 300:
            self.snake_head.goto(current_x_cor-600,current_y_cor)
        if current_x_cor == -300:
            self.snake_head.goto(current_x_cor+600,current_y_cor)
        if current_y_cor == 300:
            self.snake_head.goto(current_x_cor,current_y_cor-600)
        if current_y_cor == -300:
            self.snake_head.goto(current_x_cor,current_y_cor+600)
    def checkTailCollision(self) -> bool:
        for segments in self.snake_segments[1:]:
            if self.calculateDistance(segments.pos(),self.snake_head.pos()) < 10:
                return True
            else:
                return False
    def move(self):
        for segments_num in range(len(self.snake_segments)-1,0,-1):
            new_x = self.snake_segments[segments_num-1].xcor()
            new_y = self.snake_segments[segments_num-1].ycor()
            self.snake_segments[segments_num].goto(new_x,new_y)
        self.snake_segments[0].forward(20)
    def turn_left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)
    def turn_right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)
    def turn_up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)
    def turn_down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)
    

    