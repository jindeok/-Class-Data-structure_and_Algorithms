import numpy as np

# initialize matrix
A = np.array([[1,0,2,1], [4,1,1,0],[0,1,3,0],[2,0,1,1]])
B = np.array([[0,1,0,1], [2,1,1,4],[2,0,1,1],[1,3,5,0]])




#Strassen's algorithm

#divide matrix if len(mat) = 2^n
def StrassenDivide(mat):
    
    length = len(mat)
    
    d = length // 2
    dividedmat=[mat[:d, :d], mat[d:, :d], mat[:d, d:], mat[d:, d:]]
    
    return dividedmat
    

def StrassenProduct(mat1,mat2):
    
    #Exit recurrence if n == 1
    if (len(mat1)*len(mat2) == 1):
        
        return (mat1*mat2)
    
    else:
        #Devide to submatrices
        mat1_set = StrassenDivide(mat1)
        mat2_set = StrassenDivide(mat2)
        
        #indices for submatrices - A
        a00 = np.array(mat1_set[0])
        a01 = np.array(mat1_set[2])
        a10 = np.array(mat1_set[1])
        a11 = np.array(mat1_set[3])
        
        #indices for submatrices - B
        b00 = np.array(mat2_set[0])
        b01 = np.array(mat2_set[2])
        b10 = np.array(mat2_set[1])
        b11 = np.array(mat2_set[3])
        
        #Recursive algorithm for StrassenProduct
        m1 = np.array(StrassenProduct((a00 + a11),(b00 +b11)))
        m2 = np.array(StrassenProduct((a10 + a11), b00))
        m3 = np.array(StrassenProduct(a00,(b01 - b11)))
        m4 = np.array(StrassenProduct(a11, (b10 - b00)))
        m5 = np.array(StrassenProduct((a00 + a01), b11))
        m6 = np.array(StrassenProduct((a10 - a00), (b00 + b01)))
        m7 = np.array(StrassenProduct((a01 - a11), (b10 + b11)))
        
        #Strassen formula
        mat3_set = [m1 + m4 - m5 + m7, m3 + m5, m2 + m4, m1 + m3 - m2 + m6]
        
        mat3_set[0] = np.array((m1 + m4 - m5 + m7))
        mat3_set[2] = np.array((m3 + m5))
        mat3_set[1] = np.array((m2 + m4))
        mat3_set[3] = np.array((m1 + m3 - m2 + m6))
        
        # concatenation just for the matrix form
        concx1 = np.concatenate((mat3_set[0], mat3_set[2]),axis = 1)
        concx2= np.concatenate((mat3_set[1], mat3_set[3]),axis = 1)
        strassenresult= np.concatenate((concx1,concx2),axis = 0)
        
        return strassenresult