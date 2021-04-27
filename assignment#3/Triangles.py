import numpy as np

def splitPoints(r,q,testpoint,points): #splits points between points on the same side

	if points == []:
		return [],[]
	if q==testpoint:
		testpoint = points[0]
	side1 = []				  
	side2 = []

	for p in points:
		if(sameSide(p,testpoint,r,q)):
			side1.append(p)
		else:
			side2.append(p)

	return side1, side2

def splitPointsforBrute(r,q,points): #splits points between points on the same side

	if points == []:
		return [],[]
    
	side1 = []				  
	side2 = []
    
	cp1 = crossProduct([r[0]-q[0], r[1]-q[1], 0], [r[0]-points[0], r[1]-points[1], 0])
    
	for p in points:
		if(cp1[2]>=0):
			side1.append(p)
		else:
			side2.append(p)

	return side1, side2


def sameSide(p2,p1, r,q): # check whether it is on the same side
	cp1 = crossProduct([r[0]-q[0], r[1]-q[1], 0], [p1[0]-q[0], p1[1]-q[1], 0])
	cp2 = crossProduct([r[0]-q[0], r[1]-q[1], 0], [p2[0]-q[0], p2[1]-q[1], 0])
	if((cp1[2]*cp2[2]) > 0): # 외적 부호가 같으면 같은 쪽에 존재
		return True
	else:
		return False

def crossProduct(vec1, vec2): #Cross product : z 성분값 0 for 2-d
	result = []

	result.append(0)
	result.append(0)
	result.append(vec1[0]*vec2[1] - vec2[0]*vec1[1])

	return result

def getDistance(q,r,p):
    
    if((r[0]-q[0]) != 0):
        
        a = q[1]-r[1]
        b = r[0]-q[1]
        c = r[0]*(q[1]-r[1])/(r[0]-q[0])+q[1]
        
        dist = abs(a*p[0]+b*p[1]+c)/np.sqrt(a**2 + b**2)    
        
        return dist
    
    else: 
        return abs(p[0]-r[0]) # in the case where r[0] = q[0]