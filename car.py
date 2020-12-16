import pygame
from position import pos
from  colors import WHITE
from math import sin,cos,tan,radians,degrees,pi,atan,sqrt

class Player(pygame.sprite.Sprite):
    def __init__(self,screen,position=pos(64, 54)):
        self.screen=screen
        
        self.delta=0
        
        self.length=60
        self.width=30
        self.l_r=sqrt( pow(self.width,2)+ pow(self.length,2) )/2
        
        self.maxSteeringAngle=pi/6
        self.forwardSpeed=8

        self.forward=0
        self.canMove=True

        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('car.png').convert_alpha()
        self.image=pygame.transform.scale(img, (self.length,self.width)) 
        self.mask=pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y=position.x,position.y

        self.initial=self.image
        
        self.draw()
        self.theta=self.orientation=0

    def handle_keys(self):
        if not self.canMove:
            self.forward=0
            return

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.delta=self.maxSteeringAngle                    
        elif key[pygame.K_RIGHT]:
            self.delta=-self.maxSteeringAngle
        else:
            self.delta=0

        if key[pygame.K_UP]:
            self.forward=self.forwardSpeed
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
                
        
        self.rect.center=(x,y)
        self.orientation=theta
        self.setOrientation(self.orientation)
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, (255, 0, 0),self.rect, 2)
        pygame.draw.circle(self.screen, (0, 0, 255), self.rect.center, 2)

    def collide_with(self,obj):
        x_offset = obj.rect.left - self.rect.left
        y_offset = obj.rect.top - self.rect.top 
        
        area=self.mask.overlap_area(obj.mask, (x_offset,y_offset) ) 
        if(area<1000):
            #print("OPA")
            self.canMove=False
        else:
            #print("OK")
            pass

    
    def getDistances(self):
        
        theta=self.orientation
        if theta%pi/2==0:
            return
        x,y=self.rect.center
        
        
        
                    
        c=y-tan(-theta)*x
        
        theta_check=((theta)%(2*pi))/pi 
        if theta_check>1.5 or theta_check<0.5 :
            xn=x+20
        else:
            xn=x-20
        yn=xn*tan(-theta)+c

        pygame.draw.line(self.screen, (255,0,0), (x,y),(xn,yn), 2)
        