import pygame, sys
from  colors import *
from car import *
from track import *
from pygame.locals import *
from generations import Generation

def main():
    global play_again
    running = True

    windowLenWidth=(1200, 800)
    screen = pygame.display.set_mode(windowLenWidth)
    pygame.display.set_caption("Machine Learning Cars")
    clock = pygame.time.Clock()
    race_track=track(screen,windowLenWidth)
    pygame.init()

    clock = pygame.time.Clock()
    
    offsprings=[]
    n_generations=40
    for i in range(n_generations):
        print('Generation #'+str(i))
        if offsprings==[]:
            generation=Generation(screen,race_track,offsprings=offsprings)
        else:
            generation.updatePopulation(offsprings)

        print('starting')
        while not generation.isPopulationDead() and running==True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    play_again=False

            pygame.display.flip()          
            race_track.draw()

            #update all agents
            generation.update()
            
            pygame.display.update()
            clock.tick(30)

        generation.selectKBestParents(K=8)
        print('parents\n',generation.parents)
        generation.getMates(n_offsprings=24)
        print('mates\n',generation.mates)
        generation.combineMates()
        print('offsprings\n',generation.offsprings)
        offsprings=generation.offsprings

        if running==False:
            break
        

main()
    
