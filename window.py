import pygame
import engine
import time

pygame.init()

screen = pygame.display.set_mode((1280,700))
clock = pygame.time.Clock()





circle = engine.Object((600,300),(0,0),(0,0),1)



start = time.time()
running = True
while running:
    # draw the circle based on engine.object coordinates
    movement_circle = pygame.draw.circle(screen,"white",(circle.x,circle.y),20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if circle.veloX==0:
        circle.change_velo_x(0)
    if circle.veloY==0:
        circle.change_velo_y(0)
    if circle.acceleration_y != 0 or circle.acceleration_x != 0:
        circle.accelerate()
        pass
        
    else:
        circle.fg()
        pass
    if movement_circle.bottom >= 700:
        circle.change_velo_y(-1*circle.veloY)

    

    # work in time later
    # change_time = time.time()
    # dt = change_time-start
    # print(dt)
    dt=1
    circle.move(dt)

    # print(circle.get_position())

    # start = change_time
    pygame.display.flip()
    clock.tick(60)  
    screen.fill("black")
pygame.quit()