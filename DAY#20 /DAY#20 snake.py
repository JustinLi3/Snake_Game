import time 
from turtle import Screen  
from snake import Snake 
from food import Food 
from scoreboard import ScoreBoard
screen = Screen()  
screen.bgcolor("black")  
screen.setup(600,600) 
'''Setting title of screen''' 
screen.title("My Snake Game")   
screen.tracer(0) 
 
sam = Snake()   
food = Food() 
scoreboard = ScoreBoard()
screen.listen()
screen.onkeypress(sam.up,"Up")  
screen.onkeypress(sam.down,"Down")    
screen.onkeypress(sam.right,"Right")   
screen.onkeypress(sam.left,"Left")   
'''REMEMBER TO NOT INCLUDE PARENTHESES WHEN PUTTING A METHOD IN A METHOD''' 
'''SCREEN LISTEN RIGT BEFORE ONKEYPRESS ''' 


gameison = True 
while gameison:  
    screen.update() 
    time.sleep(0.1)  
    sam.move()    
    for segments in sam.snakelist[1:]:  
        if sam.head.distance(segments) <10:  
            sam.reset()
            scoreboard.reset()
    if sam.head.xcor() >= 300 or sam.head.xcor() <= -300 or sam.head.ycor()>=300 or sam.head.ycor()<=-300: 
        sam.reset()
        scoreboard.reset()
    elif sam.head.distance(food) <15: 
        food.refresh() 
        scoreboard.upscore() 
        sam.elongate()  
   
        





screen.exitonclick()