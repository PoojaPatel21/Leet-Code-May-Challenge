class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope1 = self.checkSlope(coordinates[0],coordinates[-1])
        for i in range(len(coordinates)-1):
            if(self.checkSlope(coordinates[i],coordinates[i+1])!=slope1):
                return False
        return True        
    def checkSlope(self,ls,ls1):
        if((ls[0]-ls1[0])!=0):
            return((ls[1]-ls1[1])/(ls[0]-ls1[0]))
        else:
            return -999
        