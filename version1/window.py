import pygame
import version1.engine as engine
import time
import random

pygame.init()

screen = pygame.display.set_mode((1280,700))
clock = pygame.time.Clock()



# engine.Object((640,350),(75,0),1,(0,0),20),engine.Object((600,350),(-75,0),1,(0,0),20)


objects = []


for x in range(5):
    mass_radius = random.randint(1,50)
    objects.append(engine.Object((random.randint(20,1260),random.randint(20,680)),(random.randint(0,100),random.randint(0,100)),mass_radius,(0,0),mass_radius))
world = engine.World(objects,1280,700)

start = time.time()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the circle based on engine.object coordinates
    for obj in objects:
        pygame.draw.circle(screen,"white",(obj.position[0],obj.position[1]),obj.radius)
    step_time = time.time()
    dt = step_time - start
    world.step(dt)




    start = step_time
    pygame.display.flip()
    clock.tick(60)  
    screen.fill("black")
pygame.quit()