from datetime import datetime
import os

class Hoover(object):

    roomSize = None # for upper-right corner coordinates
    patch_count = 0

    def __init__(self, x=0, y=0):
        # Hoover coordinates
        self.x = x
        self.y = y


    def setRoomSize(self, roomSize):
        self.roomSize = roomSize


    def goNorth(self):
        if self.y != self.roomSize[1]:
            self.y+=1


    def goSouth(self):
        if self.y != 0:
            self.y-=1


    def goEast(self):
        if self.x != self.roomSize[0]:
            self.x+=1


    def goWest(self):
        if self.x != 0:
            self.x-=1


    def executeInstruction(self, letter):
        if letter=='N':
            self.goNorth()
        elif letter=='S':
            self.goSouth()
        elif letter=='E':
            self.goEast()
        elif letter=='W':
            self.goWest()


    def getPatchCount(self):
        return self.patch_count


    def incrementPatchCount(self):
        self.patch_count+=1


    def getLocation(self):
        return [self.x, self.y]


    def showLocation(self):
        print('x: {0}, y:{1}'.format(self.x, self.y))


    def getOutput(self):
        return {'coords': self.getLocation(), 'patches': self.getPatchCount()}



def writeToStorage(myinput, myoutput):
    path = os.getcwd()

    if not os.path.exists(path+'/storage'):
        os.mkdir(path+'/storage')
    
    time_now = datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
    filename = path+'/storage/'+time_now+'.txt'

    with open(filename, 'w+') as f:
        f.write('INPUT:\n')
        f.write(str(myinput))
        f.write('\nOUTPUT:\n')
        f.write(str(myoutput))
