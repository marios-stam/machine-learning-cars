import pygame
from position import pos
from  colors import WHITE
from math import sin,cos,tan,radians,degrees,pi,atan,sqrt

class Player(pygame.sprite.Sprite):
    def __init__(self,screen,position=pos(64, 54)):
        self.screen=screen
        self.xroma=(0, 0, 128)
        self.speed=pi/10
        self.length=80
        self.width=40
        self.delta=0
        self.maxSteeringAngle=pi/6
        self.forward=0
        self.l_r=sqrt( pow(self.width,2)+ pow(self.length,2) )/2

        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('car.png').convert_alpha()
        self.image=pygame.transform.scale(img, (self.length,self.width)) 
        self.rect = self.image.get_rect()
        self.initial=self.image
        
        self.draw()
        self.theta=self.orientation=0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            print("left")  
            self.delta=self.maxSteeringAngle                    
        elif key[pygame.K_RIGHT]:
            self.delta=-self.maxSteeringAngle
        else:
            self.delta=0

        if key[pygame.K_UP]:
            self.forward=4
        else:
            self.forward=0

        if key[pygame.K_DOWN]:
            self.orientation+=pi/10
            self.setOrientation(self.orientation)

    def setOrientation(self,orient):
        self.image = pygame.transform.rotozoom(self.initial, degrees(orient)%360, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def updateDynamics(self):
        L=self.length
        delta=self.delta
        theta=self.orientation
        x,y=self.rect.center
                
        bita=atan( self.l_r*tan(delta)/L ) 

        x=x+self.forward*cos(theta+bita)
        y=y-self.forward*sin(theta+bita)
        theta=theta + self.forward*tan(delta)*cos(bita)/L
        print(self.forward*cos(theta+bita))
        
        
        self.rect.center=(x,y)
        self.orientation=theta
        self.setOrientation(self.orientation)
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0),self.rect, 2)
        pygame.draw.circle(self.screen, (0, 0, 255), self.rect.center, 2)