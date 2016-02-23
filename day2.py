"""Below is a 5x4 square grid, each of them are identical. What is the number of non-square rectangle we can have with these lines?"""

class Rectangle(object):
    def __init__(self,width,height):
        self.origin = [0,0]
        self.cursor = [0,0]
        self.count = 0
        self.width = width
        self.height = height
#        self.twoDimArray = [[0]*w for x in range(h)]
    def connectRight(self):
        if self.cursor[0] + 1 == self.width :
            return False
        else:
            self.cursor[0] = self.cursor[0] + 1
            if self.isRectangle():
                self.count = self.count + 1
            print "Right",self.origin,self.cursor,self.count
            return True
            
    def connectDown(self):
        self.cursor[1] = self.cursor[1] + 1
        self.cursor[0] = self.origin[0]
        if self.isRectangle():
            self.count = self.count + 1
        print "Down",self.origin,self.cursor,self.count
        return self.cursor[1] + 1 == self.height

    def moveOrigin(self):
        if self.origin[0] == self.width - 1:
            self.origin[0] = 0
            self.origin[1] = self.origin[1] + 1
        else:
            self.origin[0] = self.origin[0] + 1
        self.cursor[0] = self.origin[0]
        self.cursor[1] = self.origin[1]
        print "Move Origin",self.origin,self.cursor,self.count

    def shouldMoveOrigin(self):
        return self.cursor == [self.width-1,self.height-1]

    def isCompleted(self):
        return self.origin == [0,self.height]

    def isRectangle(self):
        return (self.cursor[0] - self.origin[0]) != (self.cursor[1] - self.origin[1])
    def start(self):
        while(not self.isCompleted()):
            while(self.connectRight()):
                pass
            if(self.shouldMoveOrigin()):
                self.moveOrigin()
            else:
                self.connectDown()
        print "Dimension",self.width,self.height
        print "Total rectangles:",self.count

if __name__ == "__main__":

    H = 5
    W = 4
    r = Rectangle(W,H)
    r.start()
