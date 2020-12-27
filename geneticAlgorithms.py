import random
import numpy as np
class ga():
    def __init__(self):
        pass
    @staticmethod
    def uniform_crossover(A,B):
        out=[None]*len(A)
        propabilities=np.random.rand(len(A))
        for i,p in enumerate(propabilities) :
            if p>0.5:
                out[i]=A[i]
            else:
                out[i]=B[i]
        return out

    @staticmethod
    def average_crossover(A,B,weight=0.5):
        out=[None]*len(A)
        for i in range(len(A)) :
            out[i]=weight*A[i]+(1-weight)*B[i]
        return out
    
    @staticmethod
    def addMutationstoArray(x,n_mutations=4):
        indexes=random.sample(range(0, len(x) ), n_mutations)
        for i in indexes:
            x[i]=np.random.uniform(-0.2,0.2)
        return x

    @staticmethod
    def rouletteWheelParentSelection(scoresDict):
        #print(scoresDict)
        keys=list(scoresDict.keys())
        #print(keys)
        athr=sum(keys)
        index=random.sample(range(0,int(athr)), 1)[0]
        #print('index=',index)
        i=-1
        counter=keys[i]
        while index<athr-counter:
            i-=1
            counter+=keys[i]
            #print(i)

        return keys[i]
    
if __name__ == "__main__":
    x={1:'marios', 2:'mlkas',3:'athlios',4:'themis'}
    mates=ga.getMates(x,n_offsprings=5)
    print(mates)
    """
    x=ga()
    vector=x.getWeightsVector()
    x.setWeightsFromVector()
    """

    """
    A=[1,2,3,4]
    B=[4,5,6,7]
    x=ga.average_crossover(A,B)
    print(x)
    x=ga.addMutationstoArray(x)
    print(x)
    """

    
    """
    for i in range(100):
        x={1:'marios', 2:'mlkas',3:'athlios',4:'themis'}
        i=ga.rouletteWheelParentSelection(x)
        parent1=x[i]
        x.pop(i)
        j=ga.rouletteWheelParentSelection(x)
        parent2=x[j]
        print('mate(',parent1,',',parent2,')' )
    """
    