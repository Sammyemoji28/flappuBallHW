
import pgzrun
import random

HEIGHT = 800
WIDTH = 800
TITLE = "Flappy Ball (HW)"
GRAVITY = 1000

class makeBall:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.velX = 100
        self.velY = 0
        self.radius = 40
        self.color = color
    def drawBall(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

ball = makeBall(50,50, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
ball2 = makeBall(236,60, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
ball3 = makeBall(304,94, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))

def draw():
    screen.clear() 
    ball.drawBall()
    ball2.drawBall()
    ball3.drawBall()

def update():
    pass

pgzrun.go()