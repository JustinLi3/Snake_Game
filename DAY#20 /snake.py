from turtle import Turtle 
SNAKEPOSITION = [(0,0),(-20,0),(-40,0)]  
MOVEDISTANCE = 20  

class Snake:
    def __init__(self):
        self.snakelist = []  
        self.createsnake() 
        self.head = self.snakelist[0]
        
    def createsnake(self):
        for something in SNAKEPOSITION:  
            self.add_seg(something) 
    def add_seg(self,position):
            seg =  Turtle("square") 
            seg.color("white") 
            seg.pu() 
            seg.goto(position) 
            self.snakelist.append(seg)  
    def elongate(self): 
            self.add_seg((self.snakelist[-1].xcor(), self.snakelist[-1].ycor())) 
            
    def reset(self): 
        for something in self.snakelist: 
            something.hideturtle()
        self.__init__() 
        

    def move(self): 
        for something in range(len(self.snakelist)-1, 0, -1): 
            self.snakelist[something].goto(self.snakelist[something-1].position()) 
        self.snakelist[0].forward(MOVEDISTANCE)

    def up(self):  
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self): 
        if self.head.heading()!=90: 
            self.head.setheading(270) 
    def right(self):  
        if self.head.heading()!=180:
            self.head.setheading(0) 
    def left(self):   
        if self.head.heading()!=0:
            self.head.setheading(180)