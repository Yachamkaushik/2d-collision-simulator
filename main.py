import pygame
pygame.init()
window =pygame.display.set_mode((800,800))
run=True
clock=pygame.time.Clock()
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
x=100
y=100
vx = 4
vy=2
while run:
    clock.tick(60)
    if x>=775:
        vx *= -1
    if x<=25 :
        vx *= -1
    if y>=775:
        vy *= -1
    if y<=25 :
        vy *= -1
    x+=vx
    y+=vy
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    window.fill(WHITE)
    pygame.draw.circle(window,RED,(x,y),25)
    pygame.display.flip()
pygame.quit()