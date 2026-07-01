import pygame
class Ball:
    def __init__(self,x,y,vx,vy,color,radius,mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radius = radius
        self.mass = mass
    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)
    def update(self,height,width):
        if self.x>=width-self.radius:
            self.vx*=-1
        if self.x<=self.radius:
            self.vx*=-1
        if self.y>=height-self.radius:
            self.vy*=-1
        if self.y<=self.radius:
            self.vy*=-1
        self.x += self.vx
        self.y += self.vy
    def reverse(self):
        self.vx = self.vx*-1
        self.vy = self.vy*-1