import pygame
from random import randint
import os
import time
import numpy
import math
#Importing libraries



screen = pygame.display.set_mode((500,500), flags = pygame.SCALED) #Setting the display size, along with some extra space for an extra window.

class lvl:# A class for managin the levels1

    def __init__(self):

        self.lvl1 = numpy.zeros((25,25),dtype=int) #placeholder level.
        self.lvl1[2,4] = 1
        self.lvl1[5,5] = 1
        self.lvl1[13,13] = 1
        self.lvl1[13,14] = 1
        self.lvl1[14,13] = 1
    def addborder(self, lvl): #adds a border to the level, turning all the 0s on the outside to 1s.
        for i in range(0, 25):
            lvl[i,1] = 1
            lvl[0,i] = 1
            lvl[24,i] = 1
            lvl[i,24] = 1

class plan: #Class for managing most of the 2d aspects.

    def __init__(self):

        self.gridspace = 10


    def drawgrid(self): # Draws the 25 by 25 grid, with white lines.

        global screen
        for x in range(1,25):
            pygame.draw.line(screen, (255,255,255), (x*20+502, 0), (x*20+502, 500))
        for y in range(1,25):
            pygame.draw.line(screen, (255,255,255), (501, y*20),(1002,y*20))


    def drawblock(self, lvl): #Draws the blocks on the screen where the lvl value is greater than 0

        global screen

        for x in range(0, 25):
            for y in range(0,25):

                if lvl[x,y] > 0:
                    pygame.draw.rect(screen, (255,0,0), (x*20+502, y*20, 20,20))
                
                        
class play: #class for the player.

    def __init__(self): #Variables needed for the player. Will have to chnage the y value to z when finished.
        self.x = 550
        self.y = 50
        self.angle = 90
        self.fov = 70
        self.anglereset = False

    def drawGridPlayer(self): # Draws tthe 2d player on to the grid map
    
        global screen
        pygame.draw.circle(screen, (0,255,0), (self.x, self.y), 5)

    def movement(self): #All the if statements for doing the movements for the player. Will use it for managing some of the player variables.
        pygame.mouse.set_visible(False)
        
        pygame.mouse.set_pos((250,250))
        mousex = pygame.mouse.get_pos()[0]-250
        #pygame.mouse.set_pos((250,250))
        key = pygame.key.get_pressed()
        self.angle += mousex/10
        if key[pygame.K_w] :
            self.y -=2
        if key[pygame.K_q]:
            self.angle -=1
        if key[pygame.K_s]:
            self.y +=2
        if key[pygame.K_e]:
            self.angle+=1
        if key[pygame.K_a]:
            self.x-=2
        if key[pygame.K_d]:
            self.x+=2
        if self.angle >= 360:
            self.angle = 0
        elif self.angle <= 0:
            self.angle = 360

    def DirectionalMovement(self):
        pygame.mouse.set_visible(False)
        mousex = 0
        pygame.mouse.set_pos((250,250))
        mousex = pygame.mouse.get_pos()[0]-250
        pygame.mouse.set_pos((250,250))
        self.angle+=mousex/10
        key = pygame.key.get_pressed()
        Hdist = 0
        if key[pygame.K_w]:
            Hdist = 2
            if self.angle <= 180:
                Xdist = math.cos(numpy.radians(self.angle-90))*Hdist
                Ydist = math.sin(numpy.radians(self.angle-90))*Hdist
                self.x+=Xdist
                self.y+=Ydist
            elif self.angle > 180:
                Xdist = math.cos(numpy.radians(self.angle-270))*Hdist
                Ydist = math.sin(numpy.radians(self.angle-270))*Hdist
                self.x-=Xdist
                self.y-=Ydist

        if key[pygame.K_s]:
            Hdist = 2
            if self.angle <= 180:
                Xdist = math.cos(numpy.radians(self.angle-90))*Hdist
                Ydist = math.sin(numpy.radians(self.angle-90))*Hdist
                self.x-=Xdist
                self.y-=Ydist
            elif self.angle > 180:
                Xdist = math.cos(numpy.radians(self.angle-270))*Hdist
                Ydist = math.sin(numpy.radians(self.angle-270))*Hdist
                self.x+=Xdist
                self.y+=Ydist
        
        if key[pygame.K_d]:
            Hdist = 2
            if self.angle <= 180:
                Xdist = math.cos(numpy.radians(self.angle))*Hdist
                Ydist = math.sin(numpy.radians(self.angle))*Hdist
                self.x+=Xdist
                self.y+=Ydist
            elif self.angle > 180:
                Xdist = math.cos(numpy.radians(self.angle-180))*Hdist
                Ydist = math.sin(numpy.radians(self.angle-180))*Hdist
                self.x-=Xdist
                self.y-=Ydist

        if key[pygame.K_a]:
            Hdist = 2
            if self.angle <= 180:
                Xdist = math.cos(numpy.radians(self.angle))*Hdist
                Ydist = math.sin(numpy.radians(self.angle))*Hdist
                self.x-=Xdist
                self.y-=Ydist
            elif self.angle > 180:
                Xdist = math.cos(numpy.radians(self.angle-180))*Hdist
                Ydist = math.sin(numpy.radians(self.angle-180))*Hdist
                self.x+=Xdist
                self.y+=Ydist

        if key[pygame.K_e]:
            self.angle+=2
        if key[pygame.K_q]:
            self.angle-=2
        if self.angle >= 360:
            self.angle = 0
        elif self.angle <= 0:
            self.angle = 360
    def raycastx(self, lvl): # Casts a ray using the adjacent as the x line on the 2d grid. 
        global screen
        gposx = (self.x-502)/20
        gposy = (self.y)/20
        gx = (self.x-502)-(int(gposx)*20)
        gy = (self.y) - (int(gposy)*20)

        gpo = int(gposx)
        gpb = int(gposy)
        point = 0
        
        if self.angle == 0:
            None
        elif self.angle >180:


            for i in range(0, gpo):
                    
                f = i+gpo+1
                xdist = (((gpo)*20)+502)-(i*20)
                ydist = (math.tan(numpy.radians(270-self.angle))*((i*20)+gx))
                point = [xdist, self.y+ydist]

                gpoint = [int((point[0]-502)/20), int(point[1]/20)]
                pygame.draw.line(screen, (0,0,255), [(((gpo)*20)+502)-(i*20),self.y], point)
                pygame.draw.line(screen, (0,255,0), [self.x, self.y], point) 
                
                try:
                    if lvl[gpoint[0]-1, gpoint[1]] >0:
                        break 
                except:
                    pass
            
        else:
            gx = 20-gx
            gy = 20-gy
            for i in range(0, 25-gpo):

                f = i+gpo+1
                xdist = f*20
                ydist = math.tan(numpy.radians(90-self.angle))*((i*20)+gx)
                point = [502+xdist, self.y-ydist]
                
                gpoint = [int((point[0]-502)/20), int(point[1]/20)]

                pygame.draw.line(screen, (0,0,255), [f*20+502,self.y], point)
                pygame.draw.line(screen, (0,255,0), [self.x, self.y], point)  
                
                try:
                    if lvl[gpoint[0], gpoint[1]] >0:
                        break 
                except:
                    pass
            #   print(gpoint)

    def raycasty(self, lvl): #Casts a ray uring the y axis as the adjacent instea of the x. Will use this to detect a wall on the x plane.
        global screen
        gposx = (self.x-502)/20
        gposy = (self.y)/20
        gx = (self.x-502)-(int(gposx)*20)
        gy = (self.y) - (int(gposy)*20)

        gpo = int(gposx)
        gpb = int(gposy)
        point = 0
        gpoint = 0
        tdist = 0
        width = 500/self.fov
        trueI = 0
        if self.angle==0:
            pass
        
        elif self.angle>=270 or self.angle>=0 and self.angle<=90:
            for i in range(0,gpb):
                xdist = math.tan(numpy.radians(self.angle))*(gy+(i*20))
                ydist = i*20
                point = [self.x+xdist, self.y-ydist-gy]

                gpoint = [int((point[0]-502)/20), int(point[1]/20)]
                pygame.draw.line(screen, (0,0,0), [self.x, (gpb*20)-(i*20)], point)
                pygame.draw.line(screen, (255,0,0), [self.x, self.y], point) 
                
                try: 
                    if lvl[gpoint[0], gpoint[1]-1] >0:
                        #print(gpoint)
                        tdist = math.sqrt(xdist**2+ydist**2)
                        
                        break
                except:
                    pass
            
            # if tdist == 0:
            #     return tdist
        else:
            gx = (self.x-502)-(int(gposx)*20)
            gy = (self.y) - (int(gposy)*20)
            gy=20-gy
            for i in range(0,25-gpb):
                
                f=i+gpb+1
                
                xdist = math.tan(numpy.radians(self.angle-180))*(gy+(i*20))
                ydist = (f-gpb)*20+gy
                
                point = [self.x-xdist, f*20]
                
                gpoint = [int((point[0]-502)/20), int(point[1]/20)]
                pygame.draw.line(screen, (0,255,255), [self.x, (f*20)], point)
                pygame.draw.line(screen, (255,0,0), [self.x, self.y], point)
                try:
                    if lvl[gpoint[0], gpoint[1]] >0:
                        #print(ydist)
                        #print(math.sqrt(xdist**2+ydist**2), xdist, ydist)
                        break
                except:
                    pass

    def drawOpLine(self):
        global screen
        Hdist = 25

        BXvalue = math.cos(numpy.radians(self.angle))*int(((Hdist-1)/2))
        BYvalue = math.sin(numpy.radians(self.angle))*int(((Hdist-1)/2))
        if self.angle <=180:
            Offsetx = math.cos(numpy.radians(self.angle-90))*15
            Offsety = math.sin(numpy.radians(self.angle-90))*15
            x = self.x+Offsetx
            y = self.y+Offsety
        elif self.angle >180:
            Offsetx = math.cos(numpy.radians(self.angle-270))*15
            Offsety = math.sin(numpy.radians(self.angle-270))*15
            x = self.x-Offsetx
            y = self.y-Offsety
        pygame.draw.line(screen, (255,0,255), (x-BXvalue, y-BYvalue), (x+BXvalue, y+BYvalue))
    
    def lineLength(self):
        global screen
        length = 0
        for angle in range(int(self.angle-self.fov/2), int(self.angle+self.fov/2)):
            a = 0
            if angle < 0:
                ang = 360+angle
            else:
                ang = angle
            if ang >360:
                ang = ang-360

            if ang > self.angle:
                tang = ang-self.angle
            else:
                tang = self.angle-ang
            
            length = 15/math.cos(numpy.radians(tang))
            # if tang == 0:
            #     print(length)

                
        #print(length)   

    def raycast(self, lvl):
        global screen
        
        length = 500
        xtdist = 1000000**2
        ytdist = 1000000**2
        bdist = 10000000
        adist  = 10000000
        gposx = (self.x-502)/20
        gposy = (self.y)/20
        gx = (self.x-502)-(int(gposx)*20)
        gy = (self.y) - (int(gposy)*20)
        width = int(500/self.fov)
        trueI = 0
        gpo = int(gposx)
        gpb = int(gposy)
        xpoint = 0
        ypoint = 0
        ang = 0
        Hdist = 25

        for angle in range(int(self.angle-self.fov/2), int(self.angle+self.fov/2)) :
            gx = (self.x-502)-(int(gposx)*20)
            gy = (self.y) - (int(gposy)*20)
            if angle < 0:
                ang = 360+angle
            else:
                ang = angle
            if ang >360:
                ang = ang-360

            if ang > self.angle:
                tang = ang-self.angle
            else:
                tang = self.angle-ang
            
            dist = 15/math.cos(numpy.radians(tang))
            if ang == 0 or ang == 360: # X axis wall detection
                None
            elif ang >180:


                for i in range(0, gpo):
                        

                    xdist = ((i*20)+gx)
                    ydist = (math.tan(numpy.radians(270-ang))*((i*20)+gx))
                    xpoint = [(((gpo)*20)+502)-(i*20), self.y+ydist]

                    gpoint = [int((xpoint[0]-502)/20), int(xpoint[1]/20)]
                    #pygame.draw.line(screen, (0,0,255), [(((gpo)*20)+502)-(i*20),self.y], point)
                    
                    
                    try:
                        #pygame.draw.line(screen, (0,255,0), [self.x, self.y], xpoint) 
                        if lvl[gpoint[0]-1, gpoint[1]] >0:

                            xtdist = math.sqrt((xdist)**2+(ydist)**2)
                            adist  = math.cos(numpy.radians(tang))*xtdist


                            break
                    except:
                        xtdist = 100000000000
                        pass
                
            else:
                gx = (self.x-502)-(int(gposx)*20)
                gy = (self.y) - (int(gposy)*20)
                gx = 20-gx
                gy = 20-gy
                for i in range(0, 25-gpo):

                    f = i+gpo+1
                    xdist = (i*20+gx)
                    ydist = math.tan(numpy.radians(90-ang))*((i*20)+gx)
                    xpoint = [f*20+502, self.y-ydist]
                    
                    gpoint = [int((xpoint[0]-502)/20), int(xpoint[1]/20)]

                    #pygame.draw.line(screen, (0,0,255), [f*20+502,self.y], point)
                     
                    
                    try:
                        #pygame.draw.line(screen, (0,255,0), [self.x, self.y], xpoint) 
                        if lvl[gpoint[0], gpoint[1]] >0:

                            xtdist = math.sqrt((xdist)**2+(ydist)**2)
                            adist = math.cos(numpy.radians(tang))*xtdist

                            break 
                    except:
                        xtdist = 100000000000
                        pass



            gx = (self.x-502)-(int(gposx)*20)
            gy = (self.y) - (int(gposy)*20)

            if ang==0 or ang == 360: #X axis wall detection
                None
            
            elif ang>=270 or ang>=0 and ang<=90:
                for i in range(0,gpb):
                    xdist = math.tan(numpy.radians(ang))*(gy+(i*20))
                    ydist = (gy+i*20)
                    ypoint = [self.x+xdist, self.y-ydist]

                    gpoint = [int((ypoint[0]-502)/20), int(ypoint[1]/20)]

                    

                    try: 
                        #pygame.draw.line(screen, (255,255,0), [self.x, self.y], ypoint) 
                        if lvl[gpoint[0], gpoint[1]-1] >0:
                            ytdist  = math.sqrt((xdist)**2+(ydist)**2)
                            bdist = math.cos(numpy.radians(tang))*ytdist

                            break
                    except:
                        
                        ytdist = 1000000
                        pass

                

            else:
                gx = (self.x-502)-(int(gposx)*20)
                gy = (self.y) - (int(gposy)*20)
                gy=20-gy
                for i in range(0,25-gpb):
                    f=i+gpb+1
                    xdist = math.tan(numpy.radians(ang-180))*(gy+(i*20))
                    ydist =     (gy+(i*20))
                    
                    ypoint = [self.x-xdist, f*20]
                    
                    gpoint = [int((ypoint[0]-502)/20), int(ypoint[1]/20)]

                    
                    try:
                        #pygame.draw.line(screen, (255,255,0), [self.x, self.y], ypoint)
                        if lvl[gpoint[0], gpoint[1]] >0:
                            ytdist = math.sqrt((xdist)**2+(ydist)**2)

                            bdist = math.cos(numpy.radians(tang))*ytdist
                            break   
                    except:
                        ytdist = 10000000
                        pass
            

            try:
                if ang != 0 or ang!=360:
                    if xtdist > ytdist:
                        length = 500-((bdist-dist)/800*500)
                        pygame.draw.line(screen, (255,255,255), (int(width*trueI+width), int(250-length/2)), (int(width*trueI+width), int(250+length/2)), width = int(width))
                        #print("y")
                        if ang == self.angle:
                            pygame.draw.line(screen, (0,0,0), [self.x, self.y], ypoint)
                           
                        else:
                            pygame.draw.line(screen, (255,255,0), [self.x, self.y], ypoint)
                    else:
                        length = 500-((adist-dist)/800*500)
                        #print("n")
                        pygame.draw.line(screen, (200,200,200), (int(width*trueI+width), int(250-length/2)), (int(width*trueI+width), int(250+length/2)), width = int(width))
                        if ang == self.angle:
                            pygame.draw.line(screen, (0,0,0), [self.x, self.y], xpoint)
                            
                        else:
                            pygame.draw.line(screen, (255,255,0), [self.x,self.y], xpoint)
            except:
                pass
            trueI+=1

        #print(xtdist, xpoint, ytdist, ypoint, ydist)
        #print(self.angle)


    def drawGridin(self, lvl): #highlights which grid the player is in.
        global screen
        gposx = int((self.x-502)/20)
        gposy = int((self.y)/20)

        pygame.draw.rect(screen, (100,100,100), (gposx*20+502, gposy*20, 20,20))


def main():
    clock = pygame.time.Clock()
    global screen
    #ygame.display.toggle_fullscreen()
    plane = plan()
    levels = lvl()
    player = play()
    levels.addborder(levels.lvl1)
    print(levels.lvl1)
    playing = True    
    while playing:
        clock.tick(60)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        player.DirectionalMovement()
        screen.fill((100,100,100))
        pygame.draw.rect(screen, (100,100,255), (0,0,500,250))
        pygame.draw.line(screen, (255,255,255), (501, 0), (501,500), width=3)
        player.drawGridin(levels.lvl1)
        player.drawGridPlayer()
        plane.drawgrid()
        #player.movement()
        plane.drawblock(levels.lvl1)
        player.raycast(levels.lvl1)
        player.drawOpLine()
        player.lineLength()
        #player.raycastx(levels.lvl1)
        pygame.display.update()
        pygame.display.flip()
        #player.angle+=1
        #print(player.angle)


main()




