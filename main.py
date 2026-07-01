import pygame
import ball
pygame.init()
window =pygame.display.set_mode((800,800))
run=True
clock=pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ball1=ball.Ball(100,100,5,6,BLUE,20,10)
ball2=ball.Ball(100,100,3,9,RED,20,100)
while run:
    size = window.get_size()
    clock.tick(60)
    ball1.update(size[1],size[0])
    ball2.update(size[1], size[0])
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    window.fill(WHITE)
    ball1.draw(window)
    ball2.draw(window)
    pygame.display.flip()
pygame.quit()