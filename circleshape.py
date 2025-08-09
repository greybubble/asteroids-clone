import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other_circle):
        dist = self.position.distance_to(other_circle.position)
        if dist <= self.radius + other_circle.radius:
            return True

        return False 
    
    def offscreen(self):
        return (
            self.position.x + self.radius * 3 < 0
            or self.position.y + self.radius * 3 < 0
            or self.position.x - self.radius * 3 > SCREEN_WIDTH
            or self.position.y - self.radius * 3 > SCREEN_HEIGHT
        )
