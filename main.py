import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    frame_rate = 60
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    roid = Asteroid(40, 200, 30)

    while(True):
        dt = clock.tick(frame_rate)
        dt /= 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        
        

if __name__ == "__main__":
    main()
