import pygame, sys
from  colors import *
from car import *
from track import *
from pygame.locals import *

def main():
    global play_again

    windowLenWidth=(1200, 800)
    screen = pygame.display.set_mode(windowLenWidth)
    pygame.display.set_caption("Machine Learning Cars")

    clock = pygame.time.Clock()

    race_track=track(screen,windowLenWidth)
    player = Player(screen,race_track)
    pygame.init()

    
    clock = pygame.time.Clock()

    running = True       
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                play_again=False
                                
        pygame.display.flip()
        #print(pygame.sprite.collide_mask(player,track))
        
        
        if (player.collide_with(race_track)):
            print ("OPA")
            break            
        
        race_track.draw()
        player.handle_keys()
        
        player.updateDynamics()
        
        olist = race_track.mask.outline()
        pygame.draw.lines(race_track.image,(255,0,0),1,olist) 

        olist = player.mask.outline()
        pygame.draw.lines(race_track.image,(0,255,0),1,olist) 


        player.getDistances()
        player.draw()
        pygame.display.update()
        clock.tick(30)

play_again=True
while (play_again):
    print("play again")
    main()