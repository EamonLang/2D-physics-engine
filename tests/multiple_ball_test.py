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
for x in range(10):
    objects.append(shape.Circle((random.randint(0,1280),random.randint(0,700)),(100,100),(0,0),5,20))


earth = world.World(objects,1280,700)


start = time.time()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the circle based on engine.object coordinates
    for obj in objects:
        pygame.draw.circle(screen,"white",(obj.position.x,obj.position.y),obj.radius)
    step_time = time.time()
    dt = step_time - start
    earth.step(dt)
    




    start = step_time
    pygame.display.flip()
    clock.tick(60)  
    screen.fill("black")
pygame.quit()