from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")  

class ScoreBoard(Turtle):  
    def __init__(self): 
        super().__init__()    
        self.score = 0  
        with open("hs.txt") as file: 
            self.high_score = int(file.read())
        self.pu()
        self.color("white")  
        self.goto(0,260) 
        self.hideturtle()
        self.updateScore() 
        
        
        
    def upscore(self): 
        self.score+=1 
        self.updateScore()
         
    def updateScore(self): 
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", False, align = ALIGNMENT,font = FONT)   
 
    def reset(self): 
        if(self.score>self.high_score):
            self.high_score = self.score    
            with open("hs.txt",mode = "w") as filr:
                filr.write(f"{self.high_score}")
        self.score = 0
        self.updateScore()

