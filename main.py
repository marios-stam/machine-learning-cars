import pygame, sys
from  colors import *
from car import *
from track import *
from pygame.locals import *
from generations import Generation

def main():
    global play_again

    windowLenWidth=(1200, 800)
    screen = pygame.display.set_mode(windowLenWidth)
    pygame.display.set_caption("Machine Learning Cars")
    clock = pygame.time.Clock()
    race_track=track(screen,windowLenWidth)
    pygame.init()

    clock = pygame.time.Clock()
    
    offsprings=[]
    n_generations=20
    for i in range(n_generations):
        print('Generation #'+str(i))
        generation=Generation(screen,race_track,offsprings=offsprings)

        while not generation.isPopulationDead():
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

        generation.selectKBestParents(K=10)
        print(generation.parents)
        generation.getMates(n_offsprings=20)
        print(generation.mates)
        generation.combineMates()
        print(generation.offsprings)

play_again=True
while (play_again):
    print("play again")
    main()