import pygame
import engine
import time

pygame.init()

screen = pygame.display.set_mode((1280,700))
clock = pygame.time.Clock()






obj = engine.Object((640,350),(0,0),1,(0,0))
world = engine.World([obj],1280,700)

start = time.time()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the circle based on engine.object coordinates
    movement_circle = pygame.draw.circle(screen,"white",(obj.position[0],obj.position[1]),20)
    step_time = time.time()
    dt = step_time - start
    world.step(dt)




    start = step_time
    pygame.display.flip()
    clock.tick(60)  
    screen.fill("black")
pygame.quit()