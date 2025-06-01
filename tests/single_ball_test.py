import pygame

import physics_mathlib.world as world
import physics_mathlib.shape as shape
import time
import random

pygame.init()

screen = pygame.display.set_mode((1280,700))
clock = pygame.time.Clock()






objects = []


circ = shape.Circle((640,350),(0,0),(0,0),20,20)
objects.append(circ)
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