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
