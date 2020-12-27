from car import Player
from position import pos
from geneticAlgorithms import ga

class Generation():
    def __init__(self,screen,race_track,offsprings):
        self.screen,self.track=screen,race_track
        self.scoresDict={}
        if (offsprings==[]):
            popNumber=25
            self.randomInitialise( popNumber )
            
    def randomInitialise(self,popNumber):
        population=[]
        for i in range(popNumber):
            population.append( Player(self.screen,self.track,position=pos(64+5*i, 54)) )
            
        self.population=population
        self.alive_agents=population.copy()
    
    def update(self):
        indices_to_pop=[]
        for i,player in enumerate(self.alive_agents):
            #player.handle_keys()
            player.updateDynamics()
            player.collision_check()
            player.getDistances()
            player.draw()
            player.updateScore()
            player.handleAIOutput()
        
            if player.collision_check():
                indices_to_pop.append(i)     
                

        counter=0
        for index in indices_to_pop:
            dead=self.alive_agents.pop(index-counter)
            counter+=1
            self.scoresDict[dead.score]=dead.AI.getWeightsVector()
            #self.scoresDict[dead.score]='mlkia'

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
        offsprings.append(self.parents[max(self.parents.keys())])
        for par1,par2 in mates:
            par1,par2=self.parents[par1],self.parents[par2]
            x=ga.uniform_crossover(par1,par2)
            y=ga.addMutationstoArray(x,n_mutations=10)
            offsprings.append(y)
        
        self.offsprings=offsprings

    def updatePopulation(self,offsprings):
        player=Player(self.screen,self.track,position=pos(64, 54))
        player.AI.getWeightsVector()
        weightsShapes=player.AI.weightsShapes
        
        print("population",len(self.population))
        for i,offspring in enumerate(offsprings):
            #player=self.population[i]
            print(i)
            self.population[i].AI.weightsShapes=weightsShapes
            self.population[i].AI.weightsVector=offspring
            self.population[i].AI.setWeightsFromVector()
            self.population[i].score=0
            self.population[i].rect.x=64
            self.population[i].rect.y=54
            self.population[i].old_center=self.population[i].rect.center
            self.population[i].orientation=0
            self.population[i].canMove=True
        
        self.alive_agents=self.population.copy()