import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import physics_mathlib.world as world
import physics_mathlib.shape as shape
import time
import random

pygame.init()

screen = pygame.display.set_mode((1280,700))
clock = pygame.time.Clock()




  

objects = []

rect1 = shape.Rect((640,350),(-100,0),(0,0),7,20,20)
objects.append(rect1)

rect2 = shape.Rect((600,350),(100,0),(0,0),5,20,20)
objects.append(rect2)

circ = shape.Circle((100,40),(250,-4),(0,0),25,25)
objects.append(circ)

circ2 = shape.Circle((640,100),(0,0),(0,0),30,100)
objects.append(circ2)
earth = world.World(objects,1280,700)


start = time.time()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the circle based on engine.object coordinates
    for obj in objects:
        if obj.type == 'rect':
            pygame.draw.rect(screen,"white",(obj.position.x,obj.position.y,obj.width,obj.height))
        elif obj.type == 'circle':
            pygame.draw.circle(screen,'white',(obj.position.x,obj.position.y),obj.radius)
    step_time = time.time()
    dt = step_time - start
    earth.step(dt)
    




    start = step_time
    pygame.display.flip()
    clock.tick(60)  
    screen.fill("black")
pygame.quit()