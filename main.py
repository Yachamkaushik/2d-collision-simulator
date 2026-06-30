import pygame
pygame.init()
window =pygame.display.set_mode((800,800))
run=True
clock=pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    window.fill(WHITE)
    pygame.draw.circle(window,RED,(100,100),10)
    pygame.display.flip()
pygame.quit()