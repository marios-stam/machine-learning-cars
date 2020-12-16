import pygame, sys
from  colors import *
from car import *
from track import *
from pygame.locals import *

windowLenWidth=(1200, 800)
screen = pygame.display.set_mode(windowLenWidth)
pygame.display.set_caption("Machine Learning Cars")

clock = pygame.time.Clock()

player = Player(screen)
track=track(screen,windowLenWidth)

def main():
    pygame.init()

    
    clock = pygame.time.Clock()

    running = True       
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                                
        pygame.display.flip()
        #print(pygame.sprite.collide_mask(player,track))
        
        
        player.collide_with(track)            
        
        track.draw()
        player.handle_keys()
        player.draw()
        player.updateDynamics()
        
        olist = track.mask.outline()
        pygame.draw.lines(track.image,(255,0,0),1,olist) 

        olist = player.mask.outline()
        pygame.draw.lines(track.image,(0,255,0),1,olist) 

        player.getDistances()
        pygame.display.update()
        clock.tick(30)
main()