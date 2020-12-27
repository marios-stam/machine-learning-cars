from car import Player
from position import pos
from geneticAlgorithms import ga

class Generation():
    def __init__(self,screen,race_track,offsprings):
        self.screen,self.track=screen,race_track
        self.scoresDict={}
        if (offsprings==[]):
            popNumber=20
            self.randomInitialise(popNumber)
        else:
            population=[]
            for offspring in offsprings:
                player=Player(self.screen,self.track,position=pos(64, 54))
                player.AI.weightsVector=offspring
                player.setWeightsFromVector()
                population.append( player )

            self.population=population
            self.alive_agents=population.copy()
    
    def randomInitialise(self,popNumber):
        population=[]
        for i in range(popNumber):
            population.append( Player(self.screen,self.track,position=pos(64+5*i, 54)) )
            
        self.population=population
        self.alive_agents=population.copy()
    
    def update(self):
        indices_to_pop=[]
        for i,player in enumerate(self.alive_agents):
            player.handle_keys()
            player.updateDynamics()
            player.collision_check()
            player.getDistances()
            player.draw()
            player.updateScore()
            
            if player.collision_check():
                indices_to_pop.append(i)     
                

        counter=0
        for index in indices_to_pop:
            dead=self.alive_agents.pop(index-counter)
            counter+=1
            #self.scoresDict[dead.score]=dead.AI.weightsVector
            self.scoresDict[dead.score]='mlkia'

    def isPopulationDead(self):
        return len(self.alive_agents)==0
             
    def selectKBestParents(self,K=10):
        sorted_keys=sorted(self.scoresDict.keys(),reverse=True)
        parentsDict={}
        for key in sorted_keys[:K]:
            parentsDict[key]=self.scoresDict[key]

        self.parents=parentsDict
    
    def getMates(self,n_offsprings=20):
        parentsDict=self.parents
        mates=[]
        while len(mates)<n_offsprings:
            index1=ga.rouletteWheelParentSelection(parentsDict)
             
            index2=index1
            while index1==index2:
                index2=ga.rouletteWheelParentSelection(parentsDict)
            
            mate=(index1,index2)
            if  not mate  in mates:
                mates.append(mate)

        self.mates= mates

    def combineMates(self):
        mates=self.mates
        offsprings=[]
        for par1,par2 in mates:
            x=ga.average_crossover(par1,par2)
            y=ga.addMutationstoArray(x,n_mutations=2)
            offsprings.append(y)
        
        self.offsprings=offsprings

