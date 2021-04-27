from collections import namedtuple  
import matplotlib.pyplot as plt  
import random
import Triangles
import time


Point = namedtuple('Point', 'x y')




triList = []

class ConvexHull(object): 
    
    _points = []
    _hull_points = []



    def __init__(self):
        self.r = []
        self.q = []

    def add(self, point):
        self._points.append(point)
        
    def quickHullStart(self, points):  #Setup for the QuickHull Algorithm
        #arbitrary start point
        maxY = -110 
        minY = 110
        
        for p in points:  #getting highest and lowest points (r, q)
            if p[1] > maxY:
                maxY = p[1]
                self.q = p
            if p[1] < minY:
                minY = p[1]
                self.r = p
                
        self._hull_points.append(self.r)
        self._hull_points.append(self.q)	
        points.remove(self.r)
        points.remove(self.q)
        #hull = self.r+self.q
    	
        [set0,set1] = Triangles.splitPoints(self.r,self.q,self.q,points)  #Spliting points in half by a line with the Highest and lowest points
    	
        self.quickHullAlg(set0, self.r,self.q)
        self.quickHullAlg(set1, self.r,self.q)
    
    def quickHullAlg(self, points, r, q):	
        
        furthestPoint = []       #In the inital call q and r two points with the highest and lowest y value
        maxdist = -1
            
        if points == []:
            return
    
        if len(points) == 1:
            furthestPoint = points
    
        for p in points:
            # distance btw p and line <rq>
            temp_sqrt = Triangles.getDistance(q,r,p)         
            if(temp_sqrt > maxdist):
                furthestPoint = p   #finds the furthest point from the line r, q
                maxdist = temp_sqrt
    
        if(furthestPoint == []):
            return
        
        # add to hull
        self._hull_points.append(furthestPoint) 
        points.remove(furthestPoint)
        
    
        [set0,set1] = Triangles.splitPoints(r,furthestPoint,q,points)
        [set0,set2] = Triangles.splitPoints(q,furthestPoint,r,points)
        
        
    		
        self.quickHullAlg(set1,r,furthestPoint)
        self.quickHullAlg(set2,furthestPoint, q)
        


    def get_hull_points(self):
        if self._points and not self._hull_points:
            self.quickHullStart(self._points)
            #self.bruteHullAlg(self._points)
 

        return self._hull_points
    
    
    def bruteHullAlg(self,points):
        
        maxY = -110 
        
        for p in points:  #getting highest and lowest points (r, q)
            if p[1] > maxY:
                maxY = p[1]
                self.r = p
                
        self._hull_points.append(self.r)	
        points.remove(self.r)
        
        for p in points: # pivot point
            points.remove(p)
            for w in points: # test point
                [set1,set2] = Triangles.splitPointsforBrute(self.r,p,w)
                if set1 == [] or set2 == []:
                    self._hull_points.append(p)
                   

    

    def display(self):
        # all points
        x = [p.x for p in self._points]
        y = [p.y for p in self._points]
        plt.plot(x, y, marker='D', linestyle='None')

        # hull points
        hx = [p.x for p in self._hull_points]
        hy = [p.y for p in self._hull_points]
        plt.plot(hx, hy, marker='X', linestyle='None')
        for i in range(len(hx)):
            plt.text(hx[i],hy[i],'H_p')
        

        plt.title('Convex Hull')
        plt.show()


def main():  
    ch = ConvexHull()
    numPoint = 20
    start = time.clock()  # start the time check
    for _ in range(numPoint): # tot num of Point
        ch.add(Point(random.uniform(0, 1), random.uniform(0, 1)))
        
    ch.get_hull_points()    
    print("Points on hull:", ch.get_hull_points())
    end = time.clock() # end the time check
    ch.display()
    
    print(" time consumption: ", end-start) 
    



if __name__ == '__main__':      
    main()