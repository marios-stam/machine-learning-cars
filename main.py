import pygame, sys
from  colors import *
from car import *
from pygame.locals import *

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("LEVEL 2 = Find the Correct Square!")

clock = pygame.time.Clock()

player = Player(screen)
def main():
    pygame.init()

    
    clock = pygame.time.Clock()

    running = True       
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                                
        pygame.display.flip()
        screen.fill((255, 255, 255))

        player.handle_keys()
        player.draw()
        player.updateDynamics()
        pygame.display.update()        
        clock.tick(30)
main()