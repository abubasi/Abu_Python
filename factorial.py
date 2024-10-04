# def fib(n):
#     if n<=0:
#         return []
#     series=[0,1]
#     while len(series)<n:
#         series.append(series[-1]+series[-2])
#     return series[:n]


#9.Draw a star, letter, hexagon:
#Star:
import turtle
screen=turtle.Turtle()
cir=['red','green','blue','yellow','purple']
turtle.pensize(4)
turtle.penup()
turtle.setpos(-90,30)
turtle.pendown()
for i in range(5):
    turtle.pencolor(cir[i])
    turtle.forward(200)
    turtle.right(144)
turtle.penup()
turtle.setpos(80,-140)
turtle.pendown()
turtle.pencolor("Black")
turtle.done()
#Letter:
import turtle
t=turtle.Turtle()
t.penup()
t.goto(-30,50)
t.pendown()
t.pensize(10)
t.pencolor("Black")
t.right(65)
t.forward(100)
t.setpos(-30,50)
t.right(50)
t.forward(100)
t.penup()
t.setpos(-50,-10)
t.right(65)
t.pendown()
t.backward(50)
#Hexagon:
import turtle
ttl=turtle.Turtle()
ttl.color("Light green")
ttl.begin_fill()
for j in range(6):
    ttl.forward(80)
    ttl.right(60)
ttl.end_fill()
ttl.hideturtle()
turtle.done()

# #10.Animate an object left to right:
import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Left to Right Animation")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
rect_width, rect_height = 50, 50
x = 0
y = (HEIGHT - rect_height) // 2
speed = 5
direction = 1
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += speed * direction
    if x + rect_width > WIDTH or x < 0:
        direction *= -1
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (x, y, rect_width, rect_height))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
