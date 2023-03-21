import pygame
import random
import math

'''Ball class and its functions'''
class Ball:

    def __init__(self, x, y, radius, color,velocity):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.VEL = velocity
        angle = random.randint(-53, 53)
        theta = math.radians(angle)
        self.x_vel = self.VEL*math.sin(theta)
        self.y_vel = self.VEL*math.cos(theta)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
