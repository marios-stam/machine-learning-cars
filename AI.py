import numpy as np
#from keras.layers import Dense
#from keras.models import Sequential
import random

class AI():
    def __init__(self,noofInputs=5,outputs=3):
        self.noofInputs=5
        self.createNeuralNet()

    def createNeuralNet(self,hiddenLayers=[2]):
        """Create Neural Net-#of Inputs=# of distances and 3 outputs matching ARROW_LEFT ARROW_UP ARROW_RIGHT"""
        model = Sequential()
        model.add(Dense(5, activation='relu', input_shape=(5,),bias=False ))
        for i in hiddenLayers:
            model.add(Dense(i, activation='relu',bias=False))
        model.add(Dense(3, activation='sigmoid',bias=False))
        model.compile(optimizer='adam', loss='categorical_crossentropy')
        self.model=model
           
    def predict(self,distances):
        left,up,down=self.model.predict(distances)
        print(left,up,down)

    def getWeightsVector(self):
        weights=np.array(self.model.get_weights() )
        print(weights)

        self.weightsShapes=[]
        self.weightsVector=[]
        for i in weights:
            self.weightsShapes.append(i.shape)
            vec=i.flatten()
            for j in vec:
                self.weightsVector.append(j)

        return self.weightsVector

    def setWeightsFromVector(self):
        #noflayers=len(self.weightsShape)#  # oflayers
        weights=[]
        start=0 
        for shape in self.weightsShapes:
            noofWeigths=shape[0]*shape[1]
            data=np.array( self.weightsVector[start:start+noofWeigths] )
            
            weights.append( data.reshape(shape) )
            start+=noofWeigths
        #print(self.weightsVector)
        print("================================NEW WEIGTHS================================")
        for i in weights:
            print("================================================================")               
            print(i)



